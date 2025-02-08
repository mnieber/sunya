# Glossaries

## Domain glossary

**Organizations section**: the part of the user account settings for managing your organizations

# Milestones

## MS1: The user adds an organization

1. The user highlights the checklist-item for adding their organization and clicks a link on the checklist-item card.
   1. They are redirected to the “organizations” section of their user-settings route.
2. The user submits the form to add their organization. They enter the:
   1. Organization name
   2. Display-name
   3. Member-email
      1. The user will receive organization-specific messages on the member-email address.
3. When information about other users is returned to the frontend, we always use the display_name and member_email instead of the real name and account email.
4. When the organization is added, the related check-list card is checked.
5. The card now also contains a hint to try the organization switcher.
6. Adding the organization completes the checklist item for adding your organization.

## MS2: The user switches to the new organization

1. In the organizations sectioion, a link is shown for each organization
   1. Clicking this link changes the url and activates the corresponding organization
   2. The organization links are also shown in the organization switcher on top of the page
