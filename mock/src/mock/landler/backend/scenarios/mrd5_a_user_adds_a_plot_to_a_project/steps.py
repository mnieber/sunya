import mock.landler.backend.namespace as B
from sunya import R as r, match_step as match, it


def implement_step(step):
    if match(
        step,
        it()
        .creates_the(r.plot)
        .using_the(r.polygon)
        .that_is_taken_from_the(r.api_request),
    ):
        r.polygon = B.Polygons.Models.Polygon(
            polygon="polygon",
            crc="crc",
            area=123,
        )
        r.plot = B.Plots.Models.Plot(
            name="my-plot",
            sequence_number=1,
            polygon=r.polygon,
            owner=r.project.memberships[0].organization,
        )

    elif match(step, it().creates_the(r.plot_questionnaire)):
        r.plot_questionnaire = B.PlotQuestionnaires.Models.PlotQuestionnaire(
            land_type="cropland", plot=r.plot
        )
        r.plot.plot_questionnaire = r.plot_questionnaire

    elif match(step, it().finds_the(r.default_plot_list).for_the(r.project)):
        r.default_plot_list = B.PlotLists.Models.PlotList(
            name="Default Plot List", project=r.project
        )
        r.project.plot_lists.append(r.default_plot_list)

    elif match(step, it().adds_the(r.plot).to_the(r.default_plot_list)):
        r.default_plot_list.plots.append(r.plot)
