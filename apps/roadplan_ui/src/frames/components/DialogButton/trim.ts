import { IconS } from '/src/frames/components/Icon';
import { ModeOverlayT } from '/src/utils/trim';

export type DialogButtonTrimT = {
  base: {
    componentName: string;
    root: {
      border: any;
      color: any;
      fontSize: any;
      padding: any;
    };
    Icon: {
      margin: any;
      size: any;
      color: any;
    };
  };
  danger?: ModeOverlayT<DialogButtonTrimT>;
  disabled?: ModeOverlayT<DialogButtonTrimT>;
};

export const DialogButtonS = {
  color: {
    // Modern colors (design system aligned)
    solid: () =>
      'bg-blue-600 text-white hover:bg-blue-700 active:bg-blue-800',
    outline: () =>
      'bg-white text-gray-700 hover:bg-gray-50 active:bg-gray-100',
    ghostPrimary: () =>
      'bg-transparent text-blue-600 hover:bg-blue-50 active:bg-blue-100',
    modernDisabled: () => 'opacity-50 cursor-not-allowed',
  },
  border: {
    lightGray: () => 'border border-gray-300',
    transparent: () => 'border border-transparent',
  },
  fontSize: {
    medium: () => 'text-base',
  },
  padding: {
    medium: () => 'px-4 py-2',
  },
  Icon: {
    margin: {
      medium: () => 'mr-2',
    },
    size: {
      medium: () => IconS.size.s20(),
    },
    color: {
      gray: () => IconS.color.gray(),
      white: () => IconS.color.white(),
    },
  },
};

export const DefaultDialogButtonTrim = {
  base: {
    componentName: 'Default',
    root: {
      color: DialogButtonS.color.solid(),
      border: DialogButtonS.border.transparent(),
      fontSize: DialogButtonS.fontSize.medium(),
      padding: DialogButtonS.padding.medium(),
    },
    Icon: {
      margin: DialogButtonS.Icon.margin.medium(),
      size: DialogButtonS.Icon.size.medium(),
      color: DialogButtonS.Icon.color.gray(),
    },
  },
  danger: undefined,
  disabled: {
    root: {
      color: DialogButtonS.color.modernDisabled(),
    },
  },
};
