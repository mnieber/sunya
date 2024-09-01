import { observer } from 'mobx-react-lite';
import { FormStateProvider } from 'react-form-state-context';
import { withContextProps } from 'react-props-from-context';
import { ProjectLeadT } from '/src/api/types/ProjectLeadT';
import {
  Field,
  FormCancelButton,
  FormFieldLabel,
  FormSaveButton,
  GlobalError,
  NameField,
  TextField,
} from '/src/forms/components';
import { MainFormS } from '/src/forms/components/MainForm';
import { CardS } from '/src/frames/components/Card';
import { form } from '/src/projects/components/ProjectLeadFormView/form';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './ProjectLeadFormView.scss';

export type PropsT = {
  className?: any;
  projectLead?: ProjectLeadT;
  onProjectCreated?: (projectId: string) => void;
};

export const ContextProps = {
  projectLeadsEdit: projectLeadsCtx.projectLeadsEdit,
};

export const ProjectLeadFormView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const initialValues = form.getInitialValues(props);
    const initialErrors = form.getInitialErrors(props);

    return (
      <div
        className={cn('ProjectLeadFormView', [
          CardS.padding.medium(),
          CardS.colours.default(),
          props.className,
        ])}
      >
        <FormStateProvider
          initialValues={initialValues}
          initialErrors={initialErrors}
          handleValidate={form.getHandleValidate(props)}
          handleSubmit={form.getHandleSubmit(
            props,
            initialValues,
            initialErrors
          )}
          handleCancel={form.getHandleCancel(props)}
        >
          <GlobalError className={MainFormS.GlobalError()} />

          <Field fieldName="projectLeadForm.name" className={MainFormS.Field()}>
            <FormFieldLabel label="PROJECT NAME" />
            <NameField tabIndex={1} controlled={true} autoSelect={true} />
          </Field>

          <Field
            fieldName="projectLeadForm.description"
            className={MainFormS.Field()}
          >
            <FormFieldLabel label="DESCRIPTION" />
            <TextField tabIndex={2} controlled={true} />
          </Field>

          <div className={cn(MainFormS.Buttons())}>
            <FormCancelButton
              theme="MainView"
              className={cn(MainFormS.Button.root(), MainFormS.Button.gap())}
              tabIndex={3}
              label="Cancel"
            />
            <FormSaveButton
              theme="MainView"
              tabIndex={4}
              label={props.projectLead ? 'Save project' : 'Create project'}
              className={cn(MainFormS.Button.root())}
            />
          </div>
        </FormStateProvider>
      </div>
    );
  }, ContextProps)
);
