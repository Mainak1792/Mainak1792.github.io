// Clippy implementation
class Clippy {
    constructor() {
        this.agent = null;
        this.isVisible = false;
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
        container.style.cursor = 'pointer';
        document.body.appendChild(container);

        // Create Clippy image
        const clippyImage = document.createElement('img');
        clippyImage.src = 'https://clippy.js.org/agents/CLIPPY.gif';
        clippyImage.style.width = '100px';
        clippyImage.style.height = '100px';
        container.appendChild(clippyImage);

        // Add click event
        container.addEventListener('click', () => this.toggleVisibility());
    }

    toggleVisibility() {
        if (!this.isVisible) {
            this.showMessage("Hi! I'm Clippy! How can I help you today?");
            this.isVisible = true;
        } else {
            this.hideMessage();
            this.isVisible = false;
        }
    }

    showMessage(text) {
        const messageBox = document.createElement('div');
        messageBox.id = 'clippy-message';
        messageBox.style.position = 'absolute';
        messageBox.style.bottom = '120px';
        messageBox.style.right = '0';
        messageBox.style.backgroundColor = '#fff';
        messageBox.style.padding = '10px';
        messageBox.style.borderRadius = '5px';
        messageBox.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
        messageBox.style.maxWidth = '200px';
        messageBox.textContent = text;
        document.getElementById('clippy-container').appendChild(messageBox);
    }

    hideMessage() {
        const messageBox = document.getElementById('clippy-message');
        if (messageBox) {
            messageBox.remove();
        }
    }
}

// Initialize Clippy when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.clippy = new Clippy();
}); 