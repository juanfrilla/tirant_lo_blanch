import scrapy
from portal_navarra.items import Acuerdo


class PNavarraSpider(scrapy.Spider):
    name = "pnavarraspider"
    allowed_domains = ["portalcontratacion.navarra.es"]
    start_urls = [
        "https://portalcontratacion.navarra.es/es/acuerdos-2020",
    ]

    def check_page_in_list(self, next_page):
        check_list = [f"cur={x}" for x in range(1, 5)]
        return any(subst in next_page for subst in check_list)

    def parse(self, response):
        for acuerdos in response.css("div.asset-full-content.clearfix.mb-5.no-title"):
            acuerdo = Acuerdo()
            acuerdo["fecha"] = acuerdos.css(
                """div.field-wrapper-content.lfr-forms-field-wrapper:nth-child(4)
                    > input.field.form-control::attr(value)"""
            ).get()
            acuerdo["titulo"] = (
                acuerdos.css("h2.titulo-acuerdos::text")
                .get()
                .replace("\n", "")
                .replace("  ", " ")
            )
            yield acuerdo

        next_page = response.css(
            """#_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_BbD7OO7VreZ1_ocerSearchContainerPageIterator
            > div > ul > li:nth-child(3) > a"""
        ).attrib["href"]

        if next_page is not None and self.check_page_in_list(next_page):
            yield response.follow(next_page, callback=self.parse)
