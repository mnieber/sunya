import { DefaultAuthNavHandler } from '/src/auth/routes';
import { NavHandler } from '/src/routes/navHandler';

export const createNavHandler = () => {
  const navHandler = new NavHandler();
  navHandler.installDefaultNavHandler(new DefaultAuthNavHandler());
  return navHandler;
};
