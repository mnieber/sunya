import React from 'react';
import { DefaultCardTrim, CardTrimT } from './trim';
import { cn } from '/src/utils/classnames';
import { getMode, getModeCn } from '/src/utils/trim';

export type PropsT = React.PropsWithChildren<{
  className?: any;
  trim?: CardTrimT;
}>;

export const Card: React.FC<PropsT> = (props) => {
  const { className, children, trim: propsTrim, ...rest } = props;

  const trim = propsTrim ?? DefaultCardTrim;
  const mode = getMode(trim, {});

  return (
    <div
      className={cn(
        trim.base.componentName,
        getModeCn(mode.root),
        className
      )}
      {...rest}
    >
      {children}
    </div>
  );
};
