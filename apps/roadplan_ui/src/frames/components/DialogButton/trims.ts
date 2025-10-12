import {
  DefaultDialogButtonTrim,
  DialogButtonS,
  type DialogButtonTrimT,
} from '/src/frames/components/DialogButton';
import { createTrim } from '/src/utils/trim';

export const ModernSolidDialogButtonTrim: DialogButtonTrimT = createTrim(
  DefaultDialogButtonTrim,
  {
    base: {
      componentName: 'ModernSolid-DialogButton',
      root: {
        color: DialogButtonS.color.solid(),
        border: DialogButtonS.border.transparent(),
        fontSize: DialogButtonS.fontSize.medium(),
        padding: DialogButtonS.padding.medium(),
      },
      Icon: {
        margin: DialogButtonS.Icon.margin.medium(),
        size: DialogButtonS.Icon.size.medium(),
        color: DialogButtonS.Icon.color.white(),
      },
    },
    disabled: {
      root: {
        color: DialogButtonS.color.modernDisabled(),
      },
    },
  }
);

export const ModernOutlineDialogButtonTrim: DialogButtonTrimT = createTrim(
  DefaultDialogButtonTrim,
  {
    base: {
      componentName: 'ModernOutline-DialogButton',
      root: {
        color: DialogButtonS.color.outline(),
        border: DialogButtonS.border.lightGray(),
        fontSize: DialogButtonS.fontSize.medium(),
        padding: DialogButtonS.padding.medium(),
      },
      Icon: {
        margin: DialogButtonS.Icon.margin.medium(),
        size: DialogButtonS.Icon.size.medium(),
        color: DialogButtonS.Icon.color.gray(),
      },
    },
    disabled: {
      root: {
        color: DialogButtonS.color.modernDisabled(),
      },
    },
  }
);
