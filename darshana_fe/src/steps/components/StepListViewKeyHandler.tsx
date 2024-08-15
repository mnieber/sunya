import { observer } from 'mobx-react-lite';
import * as R from 'ramda';
import React from 'react';
import KeyboardEventHandler from 'react-keyboard-event-handler';
import { withContextProps } from 'react-props-from-context';
import { createHighlightKeyHandlers } from 'skandha-facets';
import { stepsCtx } from '/src/steps/hooks/useStepsContext';
import { createKeyDownHandler } from '/src/utils';
import { cn } from '/src/utils/classnames';

export type PropsT = React.PropsWithChildren<{ className?: any }>;

const ContextProps = {
  stepsHighlight: stepsCtx.stepsHighlight,
};

export const StepListViewKeyHandler = observer(
  withContextProps((props: PropsT & typeof ContextProps) => {
    const keyHandlers = {
      ...createHighlightKeyHandlers(props.stepsHighlight),
    };
    const handledKeys = R.keys(keyHandlers);
    const onKeyDown = createKeyDownHandler(keyHandlers);

    return (
      <KeyboardEventHandler
        handleKeys={handledKeys}
        onKeyEvent={onKeyDown}
        className={cn('StepListViewKeyHandler', [props.className])}
      >
        {props.children}
      </KeyboardEventHandler>
    );
  }, ContextProps)
);
