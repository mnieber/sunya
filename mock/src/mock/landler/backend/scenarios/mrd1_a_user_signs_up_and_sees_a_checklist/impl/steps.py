import mock.landler.backend.namespace as B
from sunya import R as r, G as g, match_step as match, it


def implement_step(step):
    if match(step, it().creates_the(r.user)):
        r.user = B.Users.Models.User(email="user@example.com", password="password")

    elif match(step, it().calls_the(g.activate_user_account_action)):
        r.user.is_active = True

    elif match(step, it().sets_the_current_user_in_the(g.user_session).to(r.user)):
        g.user_session.user = r.user

    elif match(step, it().marks_the(r.user).as_authenticated()):
        r.user.is_authenticated = True

    elif match(step, it().creates_the(r.checklist).for_the(r.user)):
        # Create the checklist and assign it to the user
        r.checklist = B.Checklists.Models.Checklist(_owner=r.user)
        for name in [
            "Welcome",
            "Join the demo organization",
            "Add your organization",
            "Create a project",
            "Add a plot",
            "Trigger a project-analysis",
        ]:
            item = B.Checklists.Models.ChecklistItem(
                name=name, is_completed=False, checklist=r.checklist
            )
            r.checklist.items.append(item)

        # Set the checklist on the user
        r.user.checklist = r.checklist
