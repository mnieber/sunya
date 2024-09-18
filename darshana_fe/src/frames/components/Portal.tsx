import React from 'react';
import { createPortal } from 'react-dom';

type PropsT = React.PropsWithChildren<{
  elm: any;
}>;

export const Portal = (props: PropsT) => {
  return props.elm ? createPortal(props.children, props.elm) : null;
};
