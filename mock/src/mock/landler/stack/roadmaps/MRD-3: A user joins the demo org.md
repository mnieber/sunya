# Glossaries

## Domain glossary

**Member-email**: the email address that is used to communicate to the user in the context of (a membership of) a particular organization,

# Milestones

## MS1: At sign-up, the user is invited to the demo organization

1. When the user signs up, we automatically create an invitation to the demo organization.
   1. The send_email_cb is set to noop to prevent sending an invitation email for this case.
2. If the demo organization does not yet exist, then it is created.
   1. The demo organization already has some projects and associated plots.
3. Note that there is a single demo org shared by all users.

## MS2: The user joins the demo organization

1. The user clicks on the checklist item to join the demo organization.
   1. This takes the user to the organizations section where invites to organizations are shown
   2. When the user clicks to accept the invitation, we show a form with the following fields:
      1. Display-name
         1. In the case of a demo-organization membership, the display-name will be chosen randomly to hide the user’s identity, e.g. “busy blue horse”
         2. The user should be able to regenerate their display-name (this helps when the random name is unflattering).
      2. Member-email address
         1. The member-email for the demo organization will be based on the display name, e.g. busybluehorse@demo-org.com.
         2. Since the member-email for the demo-organization is fake, the backend will instead send email to the users main email account.
2. Joining the demo organization completes the demo organization checklist item.
3. The checklist card updates to show the link to navigate to the url of the demo-organization.
4. The checklist card also shows a link to the user’s organization settings where the user can leave the demo organization.
