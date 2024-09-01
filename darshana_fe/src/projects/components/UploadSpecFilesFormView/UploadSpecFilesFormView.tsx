import { observer } from 'mobx-react-lite';
import { FormStateProvider } from 'react-form-state-context';
import { withContextProps } from 'react-props-from-context';
import { form } from './form';
import {
  Field,
  FormCancelButton,
  FormSaveButton,
  GlobalError,
} from '/src/forms/components';
import { FileUploadFormField } from '/src/forms/components/FileUploadFormField';
import { MainFormS } from '/src/forms/components/MainForm';
import { CardS } from '/src/frames/components/Card';
import { projectCtx } from '/src/projects/hooks/useProjectContext';
import { cn } from '/src/utils/classnames';

export type PropsT = {
  className?: any;
};

export const ContextProps = {
  projectState: projectCtx.projectState,
  projectEdit: projectCtx.projectEdit,
  project: projectCtx.project,
};

export const UploadSpecFilesFormView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const initialValues = form.getInitialValues(props);
    const initialErrors = form.getInitialErrors(props);

    return (
      <div
        className={cn('UploadSpecFilesFormView', [
          CardS.colours.default,
          MainFormS.root.padding.default(),
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

          <Field fieldName="uploadForm.files" className={MainFormS.Field()}>
            <FileUploadFormField
              accept={{ 'application/yaml': ['.yaml', '.yml'] }}
              multiple={true}
            />
          </Field>

          <div className={cn(MainFormS.Buttons())}>
            <FormCancelButton
              theme="MainView"
              className={cn(MainFormS.Button.root(), MainFormS.Button.gap())}
              label="Cancel"
            />
            <FormSaveButton
              theme="MainView"
              className={cn(MainFormS.Button.root())}
              label="Upload"
            />
          </div>
        </FormStateProvider>
      </div>
    );
  }, ContextProps)
);
