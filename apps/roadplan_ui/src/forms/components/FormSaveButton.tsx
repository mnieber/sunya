import { useFormStateContext } from 'react-form-state-context';
import {
  DialogButton,
  DialogButtonPropsT,
  ModernSolidDialogButtonTrim,
} from '/src/frames/components/DialogButton';

export type PropsT = DialogButtonPropsT & {
  theme: 'MainView' | 'AuthCard';
};

export const FormSaveButton = (props: PropsT) => {
  const formState = useFormStateContext();
  const disabled = props.disabled || formState.getFlag('submitting');

  return (
    <DialogButton
      trim={ModernSolidDialogButtonTrim}
      onClick={(e: any) => {
        e.preventDefault();
        formState.submit();
      }}
      disabled={disabled}
      {...props}
    />
  );
};
