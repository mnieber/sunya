import { NavHandler } from '/src/routes/navHandler';

export const createNavHandler = () => {
  const navHandler = new NavHandler();
  // navHandler.installDefaultNavHandler(new DefaultBlogsNavHandler());
  return navHandler;
};
