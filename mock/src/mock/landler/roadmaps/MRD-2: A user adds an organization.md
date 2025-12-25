# Glossaries

## Domain glossary

**Organizations section**: the part of the user account settings for managing your organizations

# Milestones

## MS1: The user adds an organization

1. The user submits the form to add their organization. They enter the:
   1. Organization name
   2. Display-name
   3. Member-email
      1. The user will receive organization-specific messages on the member-email address.
2. When information about other users is returned to the frontend, we always use the display_name and member_email instead of the real name and account email.
3. When the organization is added, the related check-list card is checked.
4. The card now also contains a hint to try the organization switcher.

## MS2: The user switches to the new organization

1. In the organizations sectioion, a link is shown for each organization
   1. Clicking this link changes the url and activates the corresponding organization
   2. The organization links are also shown in the organization switcher on top of the page
