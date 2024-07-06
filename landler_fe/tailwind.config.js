module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      animation: {
        delete: 'pulse 1s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};
