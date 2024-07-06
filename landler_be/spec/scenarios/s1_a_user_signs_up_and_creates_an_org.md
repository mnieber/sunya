Scenario: a-user-signs-up-and-creates-an-org (s1_a_user_signs_up_and_creates_an_org.md)



# The [my-org-owner@example.com+:user] visits the [http://landler.io//sign-up:page] to create a [my-org-owner@example.com+:user]

After this step, the following actors will have been created with the following values:

my-org-owner@example.com+:user:
email=my-org-owner@example.com
id=b2cbf7e4-7b41-5414-a009-f5952a74743f
is_active=True
is_authenticated=False
password=my-password


my-org-owner@example.com+:user:
email=my-org-owner@example.com
id=b2cbf7e4-7b41-5414-a009-f5952a74743f
is_active=True
is_authenticated=False
password=my-password

## The [http://landler.io//sign-up:page] makes a [/api/accounts/sign-up/:request] to the [sign_up_user_api_view:api-view]

### The [sign_up_user_api_view:api-view] calls the [create_user:action] with the [create_user_-:form] to create a [my-org-owner@example.com+:user]

After this step, the following actors will have been created with the following values:

my-org-owner@example.com+:user:
email=my-org-owner@example.com
id=b2cbf7e4-7b41-5414-a009-f5952a74743f
is_active=False
is_authenticated=False
password=my-password

#### The [create_user:action] validates the email and password of the [create_user_-:form]

#### The [create_user:action] creates the [my-org-owner@example.com+:user]

After this step, the following actors will have been created with the following values:

my-org-owner@example.com+:user:
email=my-org-owner@example.com
id=b2cbf7e4-7b41-5414-a009-f5952a74743f
is_active=False
is_authenticated=False
password=my-password

### The [sign_up_user_api_view:api-view] activates the account of the [my-org-owner@example.com+:user]

After this step, the following actors will have been updated to the following values:

The my-org-owner@example.com+:user:
is_active=True (from False)




# The [my-org-owner@example.com+:user] visits the [http://landler.io//sign-in:page]

After this step, the following actors will have been updated to the following values:

The my-org-owner@example.com+:user:
is_authenticated=True (from False)

## The [http://landler.io//sign-in:page] makes a [/api/session/sign-in/:request] to the [sign_in_user_api_view:api-view] to sign in the [my-org-owner@example.com+:user]

After this step, the following actors will have been updated to the following values:

The my-org-owner@example.com+:user:
is_authenticated=True (from False)

### The [sign_in_user_api_view:api-view] calls the [sign_in_user:action] to sign in the [my-org-owner@example.com+:user]

After this step, the following actors will have been updated to the following values:

The my-org-owner@example.com+:user:
is_authenticated=True (from False)




# The [my-org-owner@example.com+:user] visits the [http://landler.io//user-account:page] to create an [my-org+:organization]

After this step, the following actors will have been created with the following values:

my-org+:organization:
id=4b3d6a69-7653-5dcd-bbce-0ed03d1ce2b0
memberships=['(my-org)-(my-org-owner@example.com)-(admin)+:organization-membership']
name=my-org

## The [http://landler.io//user-account:page] makes a [/api/organizations/create-organization/:request] to the [create_organization_api_view:api-view] to create an [my-org+:organization]

After this step, the following actors will have been created with the following values:

my-org+:organization:
id=4b3d6a69-7653-5dcd-bbce-0ed03d1ce2b0
memberships=['(my-org)-(my-org-owner@example.com)-(admin)+:organization-membership']
name=my-org

### The [create_organization_api_view:api-view] calls the [create_organization:action] with the [create_organization_-:form] to create a [my-org+:organization] with admin [my-org-owner@example.com+:user]

After this step, the following actors will have been created with the following values:

my-org+:organization:
id=4b3d6a69-7653-5dcd-bbce-0ed03d1ce2b0
memberships=['(my-org)-(my-org-owner@example.com)-(admin)+:organization-membership']
name=my-org

#### The [create_organization:action] creates the [my-org+:organization]

After this step, the following actors will have been created with the following values:

my-org+:organization:
id=4b3d6a69-7653-5dcd-bbce-0ed03d1ce2b0
memberships=[]
name=my-org

#### The [create_organization:action] calls the [add_user_to_organization:action] to add the [my-org-owner@example.com+:user] to the [my-org+:organization]

After this step, the following actors will have been updated to the following values:

The my-org+:organization:
memberships=['(my-org)-(my-org-owner@example.com)-(admin)+:organization-membership'] (from [])




# The [my-org-owner@example.com+:user] uses the [:organization-picker] to switch to the [http://my-org.landler.io//home:page] of the [my-org+:organization]

## The [my-org-owner@example.com+:user] is redirected to url of the [http://my-org.landler.io//home:page] which is:  http://my-org.landler.io//home

## The [:frontend] makes a [/api/session/set-active-organization:request] to the [set_active_organization_api_view:api-view] to set [my-org+:organization] as the active organization

### The [set_active_organization_api_view:api-view] updates the [:user-session] to set the active [my-org+:organization]

After this step, the following actors will have been updated to the following values:

The :user-session:
active_organization=my-org+:organization (from None)


