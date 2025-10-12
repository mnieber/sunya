import { observer } from 'mobx-react-lite';
import { withContextProps } from 'react-props-from-context';
import { nodesCtx } from '/src/treeview/hooks/useNodesContext';
import { ToolButton } from '/src/frames/components/ToolButton';
import { ModestToolButtonTrim } from '/src/frames/components/ToolButton';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  nodesZoom: nodesCtx.nodesZoom,
};

export const ZoomButton = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    return (
      <ToolButton
        className={props.className}
        trim={ModestToolButtonTrim}
        iconName={props.nodesZoom.isEnabled ? 'checkFilled' : 'checkEmpty'}
        label="Zoom"
        onClick={() => props.nodesZoom.toggle({})}
      />
    );
  }, ContextProps)
);
