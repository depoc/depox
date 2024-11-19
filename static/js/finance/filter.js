document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll('.overflow-x-auto a');

    links.forEach(link => {
        link.addEventListener('click', function (e) {

            // Remove active styles from all links
            links.forEach(link => {
                link.classList.remove(
                    'bg-blue-50', 'dark:bg-blue-950',
                    'text-blue-500', 'dark:text-blue-200',
                    'ring-blue-500', 'dark:ring-blue-500'
                );
                link.classList.add(
                    'text-black/40', 'dark:text-white/55',
                    'ring-black/10', 'dark:ring-white/20',
                    'dark:bg-primary'
                );
            });

            // Add active styles to the clicked link
            this.classList.add(
                'bg-blue-50', 'dark:bg-blue-950',
                'text-blue-500', 'dark:text-blue-200',
                'ring-blue-500', 'dark:ring-blue-500'
            );
            this.classList.remove(
                'text-black/40', 'dark:text-white/55',
                'ring-black/10', 'dark:ring-white/20',
                'dark:bg-primary'
            );
        });
    });
});
