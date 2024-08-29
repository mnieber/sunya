import 'preline';
import './App.css';

function App() {
  return (
    <header
      style={{ width: 2000 }}
      className="z-50 flex flex-wrap bg-white py-3 text-sm dark:bg-neutral-800 sm:flex-nowrap sm:justify-start sm:py-0"
    >
      <nav className="mx-auto w-full max-w-[85rem] px-4 md:px-6 lg:px-8">
        <div className="relative sm:flex sm:items-center">
          <div className="flex items-center justify-between">
            <a
              className="flex-none text-xl font-semibold text-black focus:opacity-80 focus:outline-none dark:text-white"
              href="#"
              aria-label="Brand"
            >
              Brand
            </a>
            <div className="sm:hidden">
              <button
                type="button"
                className="hs-collapse-toggle inline-flex items-center justify-center gap-x-2 rounded-lg border border-gray-200 bg-white p-2 text-gray-800 shadow-sm hover:bg-gray-50 focus:bg-gray-50 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:border-neutral-700 dark:bg-transparent dark:text-white dark:hover:bg-white/10 dark:focus:bg-white/10"
                id="hs-navbar-basic-usage-collapse"
                aria-expanded="false"
                aria-controls="hs-navbar-basic-usage"
                aria-label="Toggle navigation"
                data-hs-collapse="#hs-navbar-basic-usage"
              >
                <svg
                  className="hs-collapse-open:hidden size-4 shrink-0"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <line x1="3" x2="21" y1="6" y2="6" />
                  <line x1="3" x2="21" y1="12" y2="12" />
                  <line x1="3" x2="21" y1="18" y2="18" />
                </svg>
                <svg
                  className="hs-collapse-open:block size-4 hidden shrink-0"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M18 6 6 18" />
                  <path d="m6 6 12 12" />
                </svg>
              </button>
            </div>
          </div>

          <div
            id="hs-navbar-basic-usage"
            className="hs-collapse hidden grow basis-full overflow-hidden transition-all duration-300 sm:block"
            aria-labelledby="hs-navbar-basic-usage-collapse"
          >
            <div className="mt-5 flex flex-col gap-y-3 sm:mt-0 sm:flex-row sm:items-center sm:justify-end sm:gap-y-0 sm:ps-5">
              <a
                className="font-medium text-blue-500 focus:outline-none sm:p-2"
                href="#"
                aria-current="page"
              >
                Active
              </a>

              <div className="hs-dropdown [--adaptive:none] [--is-collapse:true] [--strategy:static]   sm:[--is-collapse:false] sm:[--strategy:absolute] ">
                <button
                  id="hs-mega-menu"
                  type="button"
                  className="hs-dropdown-toggle flex w-full items-center font-medium text-gray-600 hover:text-gray-400 focus:text-gray-400 focus:outline-none dark:text-neutral-400 dark:hover:text-neutral-500 dark:focus:text-neutral-500 sm:p-2"
                  aria-haspopup="menu"
                  aria-expanded="false"
                  aria-label="Mega Menu"
                >
                  Mega Menu
                  <svg
                    className="hs-dropdown-open:-rotate-180 sm:hs-dropdown-open:rotate-0 size-4 ms-2 shrink-0 duration-300"
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="m6 9 6 6 6-6" />
                  </svg>
                </button>

                <div
                  className="hs-dropdown-menu hs-dropdown-open:opacity-100 min-w-60 start-0 top-full z-10 hidden w-full rounded-lg bg-white py-2  opacity-0 transition-[height] duration-300 ease-in-out before:absolute dark:divide-neutral-700 dark:border-neutral-700 dark:bg-neutral-800 sm:px-2 sm:shadow-md sm:transition-[opacity,margin] sm:duration-[150ms] sm:dark:border"
                  role="menu"
                  aria-orientation="vertical"
                  aria-labelledby="hs-mega-menu"
                >
                  <div className="sm:grid sm:grid-cols-3">
                    <div className="flex flex-col">
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        About
                      </a>
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Services
                      </a>
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Customer Story
                      </a>
                    </div>

                    <div className="flex flex-col">
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Careers
                      </a>
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Careers: Overview
                      </a>
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Careers: Apply
                      </a>
                    </div>

                    <div className="flex flex-col">
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Log In
                      </a>
                      <a
                        className="flex items-center gap-x-3.5 rounded-lg px-3 py-2 text-sm text-gray-800 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-neutral-400 dark:hover:bg-neutral-700 dark:hover:text-neutral-300 dark:focus:bg-neutral-700 dark:focus:text-neutral-300"
                        href="#"
                      >
                        Sign Up
                      </a>
                    </div>
                  </div>
                </div>
              </div>

              <a
                className="font-medium text-gray-600 hover:text-gray-400 focus:text-gray-400 focus:outline-none dark:text-neutral-400 dark:hover:text-neutral-500 dark:focus:text-neutral-500 sm:p-2"
                href="#"
              >
                Project
              </a>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
}

export default App;
