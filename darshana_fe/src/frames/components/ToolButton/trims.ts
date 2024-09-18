import {
  DefaultToolButtonTrim,
  ToolButtonS,
} from '/src/frames/components/ToolButton';
import { ToolButtonTrimT } from '/src/frames/components/ToolButton/trim';
import { createTrim } from '/src/utils/trim';

export const ModestToolButtonTrim: ToolButtonTrimT = createTrim(
  DefaultToolButtonTrim,
  {
    base: {
      componentName: 'Modest-ToolButton',
      root: {},
      Icon: {
        margin: ToolButtonS.Icon.margin.none(),
        color: ToolButtonS.Icon.color.whiteFill(),
      },
    },
    disabled: {
      root: {
        color: ToolButtonS.color.whiteDisabled(),
      },
      Icon: {
        color: ToolButtonS.Icon.color.whiteFillDisabled(),
      },
    },
  }
);
