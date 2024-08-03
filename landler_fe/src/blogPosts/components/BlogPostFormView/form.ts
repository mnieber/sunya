import * as R from 'ramda';
import {
  FormState,
  HandleCancelArgsT,
  HandleSubmitArgsT,
  HandleValidateArgsT,
  unflatten,
} from 'react-form-state-context';
import { ContextProps, PropsT } from './index';
import { ObjT } from '/src/utils/types';

const getInitialValues = (props: PropsT & typeof ContextProps) => {
  return {
    'blogPostForm.title': props.blogPost.title ?? null,
    'blogPostForm.slug': props.blogPost.slug ?? null,
    'blogPostForm.content': props.blogPost.content ?? null,
    'blogPostForm.level': props.blogPost.level ?? null,
    'blogPostForm.tags': props.blogPost.tags ?? null,
  };
};

const getInitialErrors = (props: PropsT & typeof ContextProps) => {
  return {};
};

const getHandleValidate =
  (props: PropsT & typeof ContextProps) =>
  ({ values, setError }: HandleValidateArgsT) => {
    if (R.isNil(values['blogPostForm.title'])) {
      setError('blogPostForm.title', 'This field is required');
    }
  };

const getHandleSubmit =
  (
    props: PropsT & typeof ContextProps,
    initialValues: FormState['values'],
    initialErrors: FormState['errors']
  ) =>
  ({ formState, values }: HandleSubmitArgsT) => {
    return props.blogPostsEdit
      .save({
        values: unflatten({
          ...values,
          'blogPostForm.title': values['blogPostForm.title'],
          'blogPostForm.slug': values['blogPostForm.slug'],
          'blogPostForm.content': values['blogPostForm.content'],
          'blogPostForm.level': values['blogPostForm.level'],
          'blogPostForm.tags': values['blogPostForm.tags'],
        }),
      })
      .then((response: ObjT) => {
        formState.reset(initialValues, initialErrors);
        return response;
      })
      .catch((error: any) => {
        formState.setError(
          'global',
          'Oops, something went wrong, please try again later'
        );
      });
  };

const getHandleCancel =
  (props: PropsT & typeof ContextProps) =>
  ({ formState }: HandleCancelArgsT) => {
    props.blogPostsEdit.cancel();
  };

export const form = {
  getHandleValidate,
  getHandleSubmit,
  getHandleCancel,
  getInitialValues,
  getInitialErrors,
};
