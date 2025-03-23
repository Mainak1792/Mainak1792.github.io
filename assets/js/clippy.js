// Clippy implementation
class Clippy {
    constructor() {
        this.agent = null;
        this.isVisible = false;
        this.isDragging = false;
        this.currentX = 0;
        this.currentY = 0;
        this.initialX = 0;
        this.initialY = 0;
        this.xOffset = 0;
        this.yOffset = 0;
        this.messages = [
            "Hi! I'm Clippy! How can I help you today?",
            "I love helping people! What can I do for you?",
            "Did you know I can be dragged around? Try it!",
            "I'm your friendly AI assistant!",
            "Need help? Just ask!",
            "I'm here to make your day better!",
            "Want to play? Just click me!",
            "I can help you navigate the website!"
        ];
        this.currentMessageIndex = 0;
        this.init();
    }

    init() {
        // Create Clippy container
        const container = document.createElement('div');
        container.id = 'clippy-container';
        container.style.position = 'fixed';
        container.style.bottom = '20px';
        container.style.right = '20px';
        container.style.zIndex = '9999';
        container.style.cursor = 'move';
        container.style.transition = 'transform 0.2s ease';
        document.body.appendChild(container);

        // Create Clippy image
        const clippyImage = document.createElement('img');
        clippyImage.src = '/assets/images/clippy/clippy.gif';
        clippyImage.style.width = '100px';
        clippyImage.style.height = '100px';
        clippyImage.style.borderRadius = '50%';
        clippyImage.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
        container.appendChild(clippyImage);

        // Add drag events
        container.addEventListener('mousedown', (e) => this.dragStart(e));
        document.addEventListener('mousemove', (e) => this.drag(e));
        document.addEventListener('mouseup', () => this.dragEnd());

        // Add click event for messages
        container.addEventListener('click', (e) => {
            if (!this.isDragging) {
                this.toggleVisibility();
            }
        });

        // Add hover effect
        container.addEventListener('mouseenter', () => {
            container.style.transform = 'scale(1.1)';
        });

        container.addEventListener('mouseleave', () => {
            container.style.transform = 'scale(1)';
        });
    }

    dragStart(e) {
        this.initialX = e.clientX - this.xOffset;
        this.initialY = e.clientY - this.yOffset;

        if (e.target === document.getElementById('clippy-container') || 
            e.target === document.querySelector('#clippy-container img')) {
            this.isDragging = true;
        }
    }

    drag(e) {
        if (this.isDragging) {
            e.preventDefault();
            this.currentX = e.clientX - this.initialX;
            this.currentY = e.clientY - this.initialY;

            this.xOffset = this.currentX;
            this.yOffset = this.currentY;

            this.setTranslate(this.currentX, this.currentY, document.getElementById('clippy-container'));
        }
    }

    setTranslate(xPos, yPos, el) {
        el.style.transform = `translate3d(${xPos}px, ${yPos}px, 0)`;
    }

    dragEnd() {
        this.initialX = this.currentX;
        this.initialY = this.currentY;
        this.isDragging = false;
    }

    toggleVisibility() {
        if (!this.isVisible) {
            this.showMessage();
            this.isVisible = true;
        } else {
            this.hideMessage();
            this.isVisible = false;
        }
    }

    showMessage() {
        const messageBox = document.createElement('div');
        messageBox.id = 'clippy-message';
        messageBox.style.position = 'absolute';
        messageBox.style.bottom = '120px';
        messageBox.style.right = '0';
        messageBox.style.backgroundColor = '#fff';
        messageBox.style.padding = '15px';
        messageBox.style.borderRadius = '10px';
        messageBox.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
        messageBox.style.maxWidth = '250px';
        messageBox.style.fontFamily = 'Arial, sans-serif';
        messageBox.style.fontSize = '14px';
        messageBox.style.lineHeight = '1.4';
        messageBox.style.color = '#333';
        messageBox.style.animation = 'fadeIn 0.3s ease-in-out';
        
        // Add message content
        const messageText = document.createElement('div');
        messageText.textContent = this.messages[this.currentMessageIndex];
        messageBox.appendChild(messageText);

        // Add close button
        const closeButton = document.createElement('button');
        closeButton.innerHTML = '×';
        closeButton.style.position = 'absolute';
        closeButton.style.top = '5px';
        closeButton.style.right = '5px';
        closeButton.style.border = 'none';
        closeButton.style.background = 'none';
        closeButton.style.fontSize = '20px';
        closeButton.style.cursor = 'pointer';
        closeButton.style.color = '#666';
        closeButton.onclick = () => this.hideMessage();
        messageBox.appendChild(closeButton);

        document.getElementById('clippy-container').appendChild(messageBox);

        // Rotate through messages
        this.currentMessageIndex = (this.currentMessageIndex + 1) % this.messages.length;
    }

    hideMessage() {
        const messageBox = document.getElementById('clippy-message');
        if (messageBox) {
            messageBox.style.animation = 'fadeOut 0.3s ease-in-out';
            setTimeout(() => messageBox.remove(), 300);
        }
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeOut {
        from { opacity: 1; transform: translateY(0); }
        to { opacity: 0; transform: translateY(10px); }
    }
`;
document.head.appendChild(style);

// Initialize Clippy when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.clippy = new Clippy();
}); 