import * as R from 'ramda';
import {
  FormState,
  HandleCancelArgsT,
  HandleSubmitArgsT,
  HandleValidateArgsT,
} from 'react-form-state-context';
import {
  ContextProps,
  PropsT,
} from '/src/projects/components/CreateProjectFormView/CreateProjectFormView';
import { projectsNav } from '/src/projects/routes';
import { navTo } from '/src/routes/navHandler';

const getInitialValues = (props: PropsT & typeof ContextProps) => {
  return {
    'projectForm.name': props.project?.name || '',
    'projectForm.description': props.project?.description || '',
  };
};

const getInitialErrors = (props: PropsT & typeof ContextProps) => {
  return {};
};

const getHandleValidate =
  (props: PropsT & typeof ContextProps) =>
  ({ values, setError }: HandleValidateArgsT) => {
    if (
      R.isNil(values['projectForm.name']) ||
      values['projectForm.name'] === ''
    ) {
      setError('projectForm.name', 'Project name is required');
    }
  };

const getHandleSubmit =
  (
    props: PropsT & typeof ContextProps,
    initialValues: FormState['values'],
    initialErrors: FormState['errors']
  ) =>
  ({ formState, values }: HandleSubmitArgsT) => {
    return Promise.resolve()
      .then((response: any) => {
        formState.reset(initialValues, initialErrors);
        if (props.onProjectCreated) {
          props.onProjectCreated(response.id);
        }
        navTo(projectsNav.project({ projectId: response.id }));
        return response;
      })
      .catch((error: any) => {
        formState.setError(
          'global',
          'Failed to create project. Please try again.'
        );
      });
  };

const getHandleCancel =
  (props: PropsT & typeof ContextProps) =>
  ({ formState }: HandleCancelArgsT) => {
    navTo(projectsNav.projects({}));
  };

export const form = {
  getHandleValidate,
  getHandleSubmit,
  getHandleCancel,
  getInitialValues,
  getInitialErrors,
};
