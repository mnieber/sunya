import { observer } from 'mobx-react-lite';
import { isLoading } from 'mobx-resource-states';
import * as R from 'ramda';
import KeyboardEventHandler from 'react-keyboard-event-handler';
import { withContextProps } from 'react-props-from-context';
import {
  SelectionUIConnector,
  createSelectionKeyHandlers,
} from 'skandha-facets';
import { AtlasBriefT } from '/src/api/types';
import { AtlasBriefsListViewItem } from '/src/atlases/components';
import { atlasBriefsCtx } from '/src/atlases/hooks/useAtlasBriefsContext';
import { LoaderBar } from '/src/frames/components/LoaderBar';
import { L } from '/src/frames/layout';
import { createKeyDownHandler } from '/src/utils';
import { cn } from '/src/utils/classnames';

// Import styles
import './AtlasBriefsListView.scss';

export type PropsT = {
  className?: any;
};

const ContextProps = {
  atlasBriefs: atlasBriefsCtx.atlasBriefs,
  atlasBriefsSelection: atlasBriefsCtx.atlasBriefsSelection,
  atlasBriefsHighlight: atlasBriefsCtx.atlasBriefsHighlight,
};

export const AtlasBriefsListView = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    if (isLoading(props.atlasBriefs)) {
      return <AtlasBriefsListViewLoader />;
    }

    const selectionUIConnector = new SelectionUIConnector({
      selection: props.atlasBriefsSelection,
    });

    const keyHandlers = createSelectionKeyHandlers(props.atlasBriefsSelection);

    const atlasBriefDivs = props.atlasBriefs.map((atlasBrief: AtlasBriefT) => (
      <AtlasBriefsListViewItem
        key={atlasBrief.id}
        className={{
          'AtlasBriefsListViewItem--selected':
            props.atlasBriefsSelection.itemIds.includes(atlasBrief.id),
          'AtlasBriefsListViewItem--highlighted':
            props.atlasBriefsHighlight.itemId === atlasBrief.id,
        }}
        atlasBrief={atlasBrief}
        selectionUIProps={selectionUIConnector.handle(atlasBrief.id)}
      />
    ));

    return (
      <KeyboardEventHandler
        handleKeys={R.keys(keyHandlers)}
        onKeyEvent={createKeyDownHandler(keyHandlers)}
      >
        <div
          className={cn('AtlasBriefsListView', [L.col.banner()], props.className)}
          tabIndex={1}
        >
          {atlasBriefDivs}
        </div>
      </KeyboardEventHandler>
    );
  }, ContextProps)
);

export const AtlasBriefsListViewLoader = (props: { className?: any }) => {
  const loaderBars = ['1', '2', '3'].map((id: string) => {
    return <LoaderBar key={`item-${id}`} className={cn('my-1 h-6')} />;
  });

  return (
    <div
      className={cn('AtlasBriefsListViewLoader', [
        L.col.banner(),
        'min-w-[50px]',
        props.className,
      ])}
    >
      {loaderBars}
    </div>
  );
};
