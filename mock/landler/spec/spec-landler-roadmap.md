## Glossary

Checklist: the list on the home-page that guides the user in their next steps after signing up.

Organization switcher: a drop-down on the top of the page for selecting the active organization.

## Milestones

### MS1: The user signs up

1. The user visits the sign-up route and signs up
   1. They sign-up with their email address and password
2. The user receives an activation email and clicks the link to activate their account
   1. After activating their account, they are immediately signed in
      1. If the account was already active, they are redirected to the sign-in page.
3. The user is redirected to their home-page route

### MS2: The user inspects the checklist

1. The user sign-ins and is redirected to their home-page route.
2. The home-page shows a checklist of things to do next:
   1. The checklist is shown as a list of checklist-items
      1. Welcome
      2. Add your organization
      3. Create a project
      4. Add a plot
      5. Trigger a project-analysis
   2. The user can click on a checklist item to highlight it
   3. Below the checklist we show a checklist-card for the highlighted checklist-item
      1. This card contains a short explanation
      2. Every checklist-card is implemented by its own React component.
   4. The checklist-items that are completed have a checkmark
      1. The checklist-card has a button to mark the checklist item as completed
   5. The user can also hide the entire checklist
      1. This is explained on the Welcome checklist-card
      2. The Welcome checklist-card has a link to the user-settings where the visibility of the checklist can be toggled.

### MS3: The user adds an organization

1. The user clicks on the 1st checklist item to add their organization.
   1. They are redirected to the “organizations” section of their user-settings route.
2. The user submits the form to add their organization
   1. Organization name
3. For each organization, an organization link is shown
   1. Clicking this link changes the url and activates the corresponding organization
   2. The organization links are also shown in the organization switcher on top of the page
4. When the organization is added, the related checklist card is checked.
   1. The card now also contains a hint to try the organization switcher.

### MS4: The user invites a new member to their organization

1. In the organizations section, the user enters the email address and role of a new organization member and presses the “invite” button.
   1. The new member receives an email with a link to accept the invitation.
2. In the organizations section, an admin user can also change the role of another member
   1. If the admin changes their own role, then they need to confirm the change by clicking a link in a confirmation email.
3. In the organizations section, the user can also leave an organization.
