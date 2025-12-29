import sunya
from sunya import (
    goal,
    M as m,
    R as r,
    Rel as rel,
    actions as a,
    goal,
    self,
    participant,
    actor,
    note_over,
)

scenario = sunya.add_scenario(f"mrd1_a_user_signs_up")
markdown_node = sunya.add_markdown_node(scenario, "A user signs up")

markdown_node.markdown = f"""
```mermaid
sequenceDiagram
    {actor(m.External.Actors.UserSession             , role=r.UserSession)}
    {participant(m.External.Actors.Frontend          , role=r.Frontend)}
    {participant(m.Users.ApiViews.SignUpUserApiView  , role=r.SignUpUserApiView)}
    {participant(m.Users.Actions.CreateUser          , role=r.CreateUserAction)}
    {participant(m.Users.Actions.ActivateUserAccount , role=r.ActivateUserAccountAction)}
    {participant(m.Users.ApiViews.SignInUserApiView  , role=r.SignInUserApiView)}
    {participant(m.Users.Actions.SignInUser          , role=r.SignInUserAction)}

    # 🔳 Sign up
    {note_over(r.Frontend, goal(rel().sign_up_the(r.user)))}
    {r.Frontend                  >  r.SignUpUserApiView}         : {a.calls()}
    {r.SignUpUserApiView         >> r.CreateUserAction}          : {a.calls(r.create_user_form)}
    {r.CreateUserAction          >> self()}                      : {a.creates(r.user)}
    {r.CreateUserAction          >> r.SignUpUserApiView}         : {a.returns(r.user)}

    # 🔳 Activate user
    {note_over(r.SignUpUserApiView, goal(rel().activate_the(r.user_account)))}
    {r.SignUpUserApiView         >> r.ActivateUserAccountAction} : {a.calls(r.user)}
    {r.ActivateUserAccountAction >> self()}                      : {a.it(rel().activates_the(r.user))}
    {r.ActivateUserAccountAction >> r.SignUpUserApiView}         : {a.returns()}

    # 🔳 Sign in
    {note_over(r.Frontend, goal(rel().sign_in_the(r.user)))}
    {r.Frontend                  >> r.SignInUserApiView}         : {a.calls()}
    {r.SignInUserApiView         >> r.SignInUserAction}          : {a.calls(r.sign_in_user_form)}
    {r.SignInUserAction          >> self()}                      : {a.it(rel().sets_the(r.current_user).in_the(r.UserSession).to(r.user))}
    {r.SignInUserAction          >> self()}                      : {a.it(rel().marks(r.user).as_authenticated())}
    {r.SignInUserAction          >> r.SignInUserApiView}         : {a.returns()}
```
"""
