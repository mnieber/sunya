// An AuthForm has:
// - a GlobalError. This component shows an error message with some space below it.
//   Note: if there is no global error, then no error - or space - is shown.
// - a Header. This is a text above the form, e.g. 'Enter your email and password to sign in'.
// - one or more Fields. A field is a wrapper around the form-field label, the form-field
//   and the form-field-error.
// - a Button, e.g. 'Sign In'.
export const AuthFormS = {
  GlobalError: () => 'mb-4',
  Header: () => 'mb-6 text-2xl font-bold text-gray-900',
  Field: () => 'mb-4',
  Button: () => 'mt-6',
};
