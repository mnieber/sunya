import { IconS } from '/src/frames/components/Icon';
import { cn } from '/src/utils/classnames';
import { ModeOverlayT } from '/src/utils/trim';

export const ToolButtonS = {
  color: {
    white: () => cn('text-white'),
    whiteDisabled: () => cn('text-white'),
  },
  Icon: {
    size: {
      medium: () => cn([IconS.size.s32(), 'p-2']),
      small: () => cn([IconS.size.s24(), 'p-1']),
    },
    margin: {
      medium: () => cn('mr-2'),
      none: () => cn(),
    },
    color: {
      whiteFill: () => cn('fill-white'),
      whiteFillDisabled: () => cn('fill-white'),
    },
  },
};

export type ToolButtonTrimT = {
  base: {
    componentName: string;
    root: {
      color: any;
    };
    Icon: {
      margin: any;
      size: any;
      color: any;
    };
  };
  disabled?: ModeOverlayT<ToolButtonTrimT>;
};

export const DefaultToolButtonTrim = {
  // These are applied to the root element and the Icon.
  base: {
    componentName: 'ToolButton',
    root: {
      color: ToolButtonS.color.white(),
    },
    Icon: {
      size: ToolButtonS.Icon.size.medium(),
      margin: ToolButtonS.Icon.margin.medium(),
      color: ToolButtonS.Icon.color.whiteFill(),
    },
  },
  // These are layered on top if the ToolButton is disabled.
  disabled: {
    root: { color: ToolButtonS.color.whiteDisabled() },
    Icon: { color: ToolButtonS.Icon.color.whiteFillDisabled() },
  },
};
