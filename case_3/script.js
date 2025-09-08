class ImageSlider {
    constructor() {
        this.slides = document.querySelectorAll('.slide');
        this.prevBtn = document.querySelector('.prev-btn');
        this.nextBtn = document.querySelector('.next-btn');
        this.currentSlideElement = document.getElementById('current-slide');
        this.totalSlidesElement = document.getElementById('total-slides');
        this.dotsContainer = document.querySelector('.slider-dots');
        this.currentSlide = 0;
        this.totalSlides = this.slides.length;
        this.init();
    }
    init() {
        this.totalSlidesElement.textContent = this.totalSlides;
        this.createDots();
        this.showSlide(this.currentSlide);
        this.addEventListeners();
        this.startAutoSlide();
    }
    createDots() {
        for (let i = 0; i < this.totalSlides; i++) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (i === 0) dot.classList.add('active');
            dot.addEventListener('click', () => {
                this.showSlide(i);
            });
            this.dotsContainer.appendChild(dot);
        }
    }
    showSlide(index) {
        this.slides.forEach(slide => slide.classList.remove('active'));
        document.querySelectorAll('.dot').forEach(dot => dot.classList.remove('active'));
        if (index < 0) {
            this.currentSlide = this.totalSlides - 1;
        } else if (index >= this.totalSlides) {
            this.currentSlide = 0;
        } else {
            this.currentSlide = index;
        }
        this.slides[this.currentSlide].classList.add('active');
        document.querySelectorAll('.dot')[this.currentSlide].classList.add('active');
        this.currentSlideElement.textContent = this.currentSlide + 1;
    }
    nextSlide() {
        this.showSlide(this.currentSlide + 1);
    }
    prevSlide() {
        this.showSlide(this.currentSlide - 1);
    }
    addEventListeners() {
        this.nextBtn.addEventListener('click', () => {
            this.nextSlide();
            this.resetAutoSlide();
        });
        this.prevBtn.addEventListener('click', () => {
            this.prevSlide();
            this.resetAutoSlide();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight') {
                this.nextSlide();
                this.resetAutoSlide();
            } else if (e.key === 'ArrowLeft') {
                this.prevSlide();
                this.resetAutoSlide();
            }
        });
    }
    startAutoSlide() {
        this.autoSlideInterval = setInterval(() => {
            this.nextSlide();
        }, 5000);
    }
    resetAutoSlide() {
        clearInterval(this.autoSlideInterval);
        this.startAutoSlide();
    }
}
document.addEventListener('DOMContentLoaded', () => {
    new ImageSlider();
});