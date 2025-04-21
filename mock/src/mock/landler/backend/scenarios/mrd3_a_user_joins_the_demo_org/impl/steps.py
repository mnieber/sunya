import mock.landler.backend.namespace as B
from sunya import R as r, G as g, match_step as match, it


def implement_step(step):
    if match(step, it().creates_the(r.demo_organization)):
        r.demo_organization = B.Organizations.Models.Organization(name="demo")
        r.demo_organization.staff_settings = (
            B.Organizations.Models.OrganizationStaffSettings(
                is_managed_by_tlg=True,
                is_demo_org=True,
                organization=r.demo_organization,
            )
        )

    elif match(
        step,
        it()
        .creates_the(r.demo_organization_membership)
        .using_the(g.generate_random_display_name_rule),
    ):
        r.demo_organization_membership = B.Organizations.Models.OrganizationMembership(
            role="EDITOR",
            display_name="busy-blue-horse",
            member_email="busy-blue-horse@demo-org.com",
            organization=r.demo_organization,
            user=g.user_session.user,
        )
        r.demo_organization.memberships.append(r.demo_organization_membership)

    if match(step, it().finds_the(r.join_demo_org_checklist_item).for_the(r.user)):
        for item in r.user.checklist.items:
            if item.name == "Join the demo organization":
                r.join_demo_org_checklist_item = item
                break

    elif match(step, it().marks_the(r.join_demo_org_checklist_item).as_completed()):
        r.join_demo_org_checklist_item.is_completed = True
