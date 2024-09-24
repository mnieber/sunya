# Glossaries

## Domain glossary

**Member-email**: the email address that is used to communicate to the user in the context of (a membership of) a particular organization,

# Milestones

## MS1: The user joins the demo organization

1. The user clicks on the checklist item to join the demo org.
   1. Note that there is a single demo org shared by all users.
   2. The demo organization already has some projects and associated plots.
2. For every organization membership, we store a display-name.
   1. In the case of a demo-organization membership, the display-name will be chosen randomly to hide the user’s identity.
      1. E.g. the display name might be “busy blue horse”
      2. The user should be able to regenerate their display-name (this helps when the random name is unflattering).
      3. The member-email for the demo organization will be based on the display name, e.g. busybluehorse@demo-org.com.
         1. Instead of sending emails to this particular (fake) member-email, the backend will instead send it to the users main email account.
   2. When information about other users is returned to the frontend, we always use the display_name and member_email instead of the real name and account email.
3. Joining the demo organization should complete the demo organization checklist item.
   1. The checklist card updates to show the link to navigate to the url of the demo-organization.
   2. The checklist card also shows a link to the user’s organization settings where the user can leave the demo organization.

## MS2: The user adds an organization

1. The user highlights the checklist-item for adding their organization and clicks a link on the checklist-item card.
   1. They are redirected to the “organizations” section of their user-settings route.
2. The user submits the form to add their organization. They enter the:
   1. Organization name
   2. Display-name
   3. Member-email
      1. The user will receive organization-specific messages on this email address.
3. For each organization, an organization link is shown
   1. Clicking this link changes the url and activates the corresponding organization
   2. The organization links are also shown in the organization switcher on top of the page
4. When the organization is added, the related check-list card is checked.
   1. The card now also contains a hint to try the organization switcher.
   2. Adding the organization should complete the checklist item for adding your organization.
