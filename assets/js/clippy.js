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
            "Hello! I'm your AI research assistant. How can I help you today?",
            "I can help you navigate through my research publications and projects.",
            "Did you know I'm a PhD candidate in AI at IIT Delhi?",
            "Feel free to explore my teaching and research work!",
            "I specialize in AI-driven signal processing and multi-modal learning.",
            "Want to learn about my latest research in structural vibration-based recognition?",
            "I'm here to help you understand my academic journey and achievements.",
            "Check out my publications and conference presentations!"
        ];
        this.currentMessageIndex = 0;
        this.usedMessages = new Set();
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
        container.style.transition = 'all 0.3s ease';
        container.style.filter = 'drop-shadow(0 4px 6px rgba(0,0,0,0.1))';
        document.body.appendChild(container);

        // Create Clippy image
        const clippyImage = document.createElement('img');
        clippyImage.src = '/assets/images/clippy/clippy.gif';
        clippyImage.style.width = '80px';
        clippyImage.style.height = '80px';
        clippyImage.style.borderRadius = '50%';
        clippyImage.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
        clippyImage.style.border = '2px solid #ffffff';
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
            container.style.transform = 'scale(1.05) translateY(-5px)';
            container.style.filter = 'drop-shadow(0 6px 8px rgba(0,0,0,0.15))';
        });

        container.addEventListener('mouseleave', () => {
            container.style.transform = 'scale(1) translateY(0)';
            container.style.filter = 'drop-shadow(0 4px 6px rgba(0,0,0,0.1))';
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
        if (this.usedMessages.size >= this.messages.length) {
            this.usedMessages.clear();
        }

        let nextIndex;
        do {
            nextIndex = Math.floor(Math.random() * this.messages.length);
        } while (this.usedMessages.has(nextIndex));

        this.usedMessages.add(nextIndex);
        const message = this.messages[nextIndex];

        const messageBox = document.createElement('div');
        messageBox.id = 'clippy-message';
        messageBox.style.position = 'absolute';
        messageBox.style.bottom = '100px';
        messageBox.style.right = '0';
        messageBox.style.backgroundColor = '#ffffff';
        messageBox.style.padding = '15px 20px';
        messageBox.style.borderRadius = '12px';
        messageBox.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
        messageBox.style.maxWidth = '280px';
        messageBox.style.fontFamily = 'system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';
        messageBox.style.fontSize = '14px';
        messageBox.style.lineHeight = '1.5';
        messageBox.style.color = '#2c3e50';
        messageBox.style.animation = 'fadeIn 0.3s ease-in-out';
        messageBox.style.border = '1px solid rgba(0,0,0,0.05)';
        
        // Add message content
        const messageText = document.createElement('div');
        messageText.textContent = message;
        messageText.style.marginBottom = '8px';
        messageBox.appendChild(messageText);

        // Add close button
        const closeButton = document.createElement('button');
        closeButton.innerHTML = '×';
        closeButton.style.position = 'absolute';
        closeButton.style.top = '8px';
        closeButton.style.right = '8px';
        closeButton.style.border = 'none';
        closeButton.style.background = 'none';
        closeButton.style.fontSize = '18px';
        closeButton.style.cursor = 'pointer';
        closeButton.style.color = '#95a5a6';
        closeButton.style.padding = '0 4px';
        closeButton.style.lineHeight = '1';
        closeButton.style.transition = 'color 0.2s ease';
        closeButton.onmouseover = () => closeButton.style.color = '#2c3e50';
        closeButton.onmouseout = () => closeButton.style.color = '#95a5a6';
        closeButton.onclick = () => this.hideMessage();
        messageBox.appendChild(closeButton);

        document.getElementById('clippy-container').appendChild(messageBox);
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
        from { 
            opacity: 0; 
            transform: translateY(10px);
        }
        to { 
            opacity: 1; 
            transform: translateY(0);
        }
    }
    @keyframes fadeOut {
        from { 
            opacity: 1; 
            transform: translateY(0);
        }
        to { 
            opacity: 0; 
            transform: translateY(10px);
        }
    }
`;
document.head.appendChild(style);

// Initialize Clippy when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.clippy = new Clippy();
}); 