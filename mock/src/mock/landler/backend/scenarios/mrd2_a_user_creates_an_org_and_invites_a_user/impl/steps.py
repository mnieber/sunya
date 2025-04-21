import mock.landler.backend.namespace as B
from sunya import R as r, G as g, match_step as match, it


def implement_step(step):
    if match(step, it().finds_the(r.create_org_checklist_item).for_the(r.user)):
        for item in r.user.checklist.items:
            if item.name == "Add your organization":
                r.create_org_checklist_item = item
                break

    elif match(step, it().marks_the(r.create_org_checklist_item).as_completed()):
        r.create_org_checklist_item.is_completed = True

    elif match(step, it().creates_the(r.organization)):
        r.organization = B.Organizations.Models.Organization(name="my-org")
        r.organization.staff_settings = (
            B.Organizations.Models.OrganizationStaffSettings(
                is_managed_by_tlg=False, is_demo_org=False, organization=r.organization
            )
        )

    elif match(step, it().creates_the(r.organization_membership)):
        r.organization_membership = B.Organizations.Models.OrganizationMembership(
            role=B.Organizations.Enums.UserInOrganizationRoles.ADMIN,
            display_name=r.user.email.split("@")[0],
            member_email=r.user.email,
            organization=r.organization,
            user=r.user,
        )
        r.organization.memberships.append(r.organization_membership)

    elif match(
        step,
        it().sets(r.organization).as_the_active_organization_in_the(g.user_session),
    ):
        g.user_session.active_organization = r.organization
