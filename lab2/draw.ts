class Click {
    private _x: number;
    private _y: number;

    constructor(x: number, y: number) {
        this._x = x;
        this._y = y;
    }

    get x() {
        return this._x;
    }

    get y() {
        return this._y;
    }
}

class Grid {
    private _n: number;
    private _m: number;
    private _colorValues: string[][];
    private _defaultColor: string = "white";

    constructor(n: number, m: number) {
        this._n = n;
        this._m = m;
        this._colorValues = new Array(n);
        for (let i = 0; i < this.n; i++) {
            this._colorValues[i] = new Array(m);
        }
        this.setAll(this._defaultColor)
    }

    setAll(color: string) {
        for (let i = 0; i < this._n; i++) {
            for (let j = 0; j < this._m; j++) {
                this._colorValues[i][j] = this._defaultColor
            }
        }
    }

    update(boxSize: number, click: Click, color: string = "black") {
        this._colorValues[Math.floor(click.y / boxSize)][Math.floor(click.x / boxSize)] = color;
    }

    get n(): number {
        return this._n;
    }

    get m(): number {
        return this._m;
    }

    get colorValues(): string[][] {
        return this._colorValues;
    }


    set colorValues(value: string[][]) {
        this._colorValues = value;
    }
}


class Canvas {
    private height: number;
    private width: number;
    private canvasElement: HTMLCanvasElement;
    private context: CanvasRenderingContext2D | null;
    private boxSize: number;
    private grid: Grid;
    private _drawColor: string;

    constructor(height: number, width: number, canvasElement: HTMLCanvasElement, boxSize: number = 50, drawColor: string = "black") {
        this.height = height;
        this.width = width;
        this.canvasElement = canvasElement;
        this.context = this.canvasElement.getContext("2d");
        if (this.context == null) {
            throw new Error("Failed to init context")
        }
        this.context.lineCap = 'round';
        this.context.lineJoin = 'round';
        this.context.strokeStyle = 'black';
        this.context.lineWidth = 1;
        this.grid = new Grid(Math.floor(height / boxSize), Math.floor(width / boxSize));
        this.boxSize = boxSize;
        this._drawColor = drawColor;
        this.canvasElement.width = width;
        this.canvasElement.height = height;

        this.redraw();
        this.createUserEvents();
        console.log(this);
    }

    private redraw() {
        if (this.context == null) {
            throw new Error("Failed to init context")
        }
        let colorValues = this.grid.colorValues;
        let yOffset = 0;
        for (let i = 0; i < this.grid.n; i++) {
            let xOffset = 0;
            for (let j = 0; j < this.grid.m; j++) {

                let styleBefore = this.context.fillStyle;
                this.context.fillStyle = colorValues[i][j];
                this.context.fillRect(xOffset, yOffset, xOffset + this.boxSize, yOffset + this.boxSize);
                xOffset += this.boxSize;
                this.context.fillStyle = styleBefore;
            }
            yOffset += this.boxSize;
        }
    }

    private createUserEvents() {
        this.canvasElement.addEventListener("mouseup", (e: MouseEvent) => this.clickEvent(e));
    }


    private clickEvent(e: MouseEvent) {
        console.log(e);
        console.log(this);
        let mouseX = e.pageX;
        let mouseY = e.pageY;
        mouseX -= this.canvasElement.offsetLeft;
        mouseY -= this.canvasElement.offsetTop;

        this.grid.update(this.boxSize, new Click(mouseX, mouseY), this._drawColor);
        this.redraw()
    }


    set drawColor(value: string) {
        this._drawColor = value;
    }
}

class ColorPicker {
    private div: HTMLDivElement;
    private canvas: Canvas;


    constructor(div: HTMLDivElement, canvas: Canvas) {
        this.div = div;
        this.canvas = canvas;


        let radioGroup: string = "colorPicker";

        let blackRadio: HTMLInputElement = ColorPicker.getRadioButton("black", radioGroup, this.canvas, true);
        let greenRadio: HTMLInputElement = ColorPicker.getRadioButton("green", radioGroup, this.canvas);
        let blueRadio: HTMLInputElement = ColorPicker.getRadioButton("blue", radioGroup, this.canvas);
        let whiteRadio: HTMLInputElement = ColorPicker.getRadioButton("white", radioGroup, this.canvas);
        let radioForm: HTMLFormElement = document.createElement('form') as HTMLFormElement;
        [blackRadio, greenRadio, blueRadio, whiteRadio].forEach(btn => {
            radioForm.appendChild(btn);
            radioForm.appendChild(document.createTextNode(btn.value))
        });
        this.div.appendChild(radioForm);

    }

    private static getRadioButton(color: string, group: string, canvas: Canvas, picked: boolean = false): HTMLInputElement {
        let radioBtn = document.createElement('input') as HTMLInputElement;
        radioBtn.type = "radio";
        radioBtn.name = group;
        radioBtn.value = color;
        if (picked) {
            radioBtn.checked = true;
        }
        radioBtn.onclick = () => {
            canvas.drawColor = radioBtn.value;
        };
        return radioBtn;
    }
}