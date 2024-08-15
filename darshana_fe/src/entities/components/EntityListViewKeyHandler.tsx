import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import KeyboardEventHandler from 'react-keyboard-event-handler';
import { withContextProps } from 'react-props-from-context';
import { createSelectionKeyHandlers } from 'skandha-facets';
import { entitiesCtx } from '/src/entities/hooks/useEntitiesContext';
import { createKeyDownHandler } from '/src/utils';
import { cn } from '/src/utils/classnames';

export type PropsT = React.PropsWithChildren<{ className?: any }>;

const ContextProps = {
  entitiesSelection: entitiesCtx.entitiesSelection,
};

export const EntityListViewKeyHandler = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const keyHandlers = {
      ...createSelectionKeyHandlers(props.entitiesSelection),
    };
    const handledKeys = R.keys(keyHandlers);
    const onKeyDown = createKeyDownHandler(keyHandlers);

    return (
      <KeyboardEventHandler
        handleKeys={handledKeys}
        onKeyEvent={onKeyDown}
        className={cn('EntityListViewKeyHandler', [props.className])}
      >
        {props.children}
      </KeyboardEventHandler>
    );
  }, ContextProps)
);
