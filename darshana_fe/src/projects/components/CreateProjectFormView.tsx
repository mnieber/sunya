import { observer } from 'mobx-react-lite';
import { FormStateProvider } from 'react-form-state-context';
import { withContextProps } from 'react-props-from-context';
import {
  Field,
  FormCancelButton,
  FormFieldLabel,
  FormSaveButton,
  GlobalError,
  NameField,
} from '/src/forms/components';
import { FileUploadFormField } from '/src/forms/components/FileUploadFormField';
import { MainFormS } from '/src/forms/components/MainForm';
import { CardS } from '/src/frames/components/Card';
import { projectLeadsCtx } from '/src/projects/hooks/useProjectLeadsContext';
import { cn } from '/src/utils/classnames';

// Import styles
import './CreateProjectFormView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  projectLeadsState: projectLeadsCtx.projectLeadsState,
};

export const CreateProjectFormView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    // Form handlers (to be implemented)
    const handleSubmit = () => {
      return Promise.resolve();
    };

    const handleCancel = () => {
      // Implement cancel logic
    };

    return (
      <div
        className={cn('CreateProjectFormView', [
          CardS.padding.medium,
          CardS.colours.default,
          props.className,
        ])}
      >
        <FormStateProvider
          initialValues={{
            'projectForm.name': '',
            'projectForm.specFiles': [],
          }}
          initialErrors={{}}
          handleSubmit={handleSubmit}
          handleCancel={handleCancel}
        >
          <GlobalError className={MainFormS.GlobalError()} />

          <Field fieldName="projectForm.name" className={MainFormS.Field()}>
            <FormFieldLabel label="PROJECT NAME" />
            <NameField tabIndex={1} controlled={true} autoSelect={true} />
          </Field>

          <Field
            fieldName="projectForm.specFiles"
            className={MainFormS.Field()}
          >
            <FormFieldLabel label="UPLOAD SPEC FILES" />
            <FileUploadFormField
              accept={{ 'application/x-yaml': ['.yaml', '.yml'] }}
              multiple={true}
            />
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
              label="Create Project"
              className={cn(MainFormS.Button.root())}
            />
          </div>
        </FormStateProvider>
      </div>
    );
  }, ContextProps)
);
