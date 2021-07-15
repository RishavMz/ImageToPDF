#include<windows.h>
#include<stdio.h>
#include <commdlg.h>      // To allow GetOpenFileName

#define GET_FILENAME 1 
#define ADD_IMAGE 2
#define MAX_IMAGES 200

LRESULT CALLBACK windowProcedure(HWND, UINT, WPARAM, LPARAM);     // Declare event loop

void AddControls(HWND);
void openFile(HWND);

HWND hEdit;
HWND Selected;
wchar_t IMAGES_ADDED[5000];
char images_selected[5000];
int imptr = 0;
int imgs = 0;

// Main method for GUI application
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow)
{
    // Initializing data for creating window
    WNDCLASSW w = {0};
    w.hbrBackground = (HBRUSH)COLOR_WINDOW;
    w.hCursor = LoadCursor(NULL, IDC_ARROW);
    w.hInstance = hInst;
    w.lpszClassName = L"PDFconverter";
    w.lpfnWndProc = windowProcedure;

    // Create window if everything OK
    if(!RegisterClassW(&w))
        return -1;
    CreateWindow("PDFconverter","Image To PDF Converter", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100, 100, 500, 500, NULL, NULL, NULL, NULL);
    
    MSG msg = {0};
    while(GetMessage(&msg, NULL, NULL, NULL))       // Run event loop and handle messages and events
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK windowProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp)       // Define event loop
{
    switch (msg)                                // Handles messages
    {
        case WM_COMMAND:                        // Handles specific commands
            switch(wp)
            {
                case GET_FILENAME:              // Prints the filename
                    wchar_t text[200];
                    GetWindowTextW(hEdit, text, 200);
                    for(int i=0; i<200; i++)
                    {
                        if(text[i]=='\0')
                            break;
                        printf("%c",text[i]);
                    }
                    break;

                case ADD_IMAGE:                 // Adds one image at once to the temporary variable
                    openFile(hWnd);
                    break;    
            }
            break;
        case WM_CREATE:                         // Called when the window created
            AddControls(hWnd);
            break;
        case WM_DESTROY:                        // Called when the Window closed
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProcW(hWnd, msg, wp, lp);   // Ignore event
    }


}

void AddControls(HWND hWnd)                     // Add elements to window
{
    CreateWindowW(L"Static", L"Enter filename : ", WS_VISIBLE | WS_CHILD, 70, 50, 150, 50, hWnd, NULL, NULL, NULL);
    hEdit = CreateWindowW(L"Edit", L"sample", WS_VISIBLE | WS_CHILD, 210, 47, 200, 25, hWnd, NULL, NULL, NULL );
    Selected = CreateWindowW(L"Static", IMAGES_ADDED, WS_VISIBLE | WS_CHILD | WS_BORDER, 70, 100, 350, 250, hWnd, NULL, NULL, NULL);
    CreateWindowW(L"Button", L"CONVERT", WS_VISIBLE | WS_CHILD, 300, 400, 100, 25, hWnd, (HMENU) GET_FILENAME , NULL, NULL );
    CreateWindowW(L"Button", L"ADD IMAGE", WS_VISIBLE | WS_CHILD, 100, 400, 100, 25, hWnd, (HMENU) ADD_IMAGE , NULL, NULL );
}

void openFile(HWND hWnd)                        // Handle opening of file
{
    OPENFILENAME op;
    char file_name[200];                        // Individual file path size

    ZeroMemory(&op, sizeof(OPENFILENAME));
    op.lStructSize = sizeof(OPENFILENAME);
    op.hwndOwner = hWnd;
    op.lpstrFile = file_name;
    op.lpstrFile[0] = '\0';
    op.nMaxFile = 400;                          // Buffer size (MAX)
    op.lpstrFilter = "All files\0*.*\0PNG\0*.png\0JPEG\0*.jpeg\0JPG\0jpg\0";
    op.nFilterIndex = 1;

    if(imgs++ < MAX_IMAGES)
        GetOpenFileName(&op);                       // Opens the SELECT FILE window

    for(int i=0; i<200; i++)                        // Insert characters from buffer to required character array
    {
        if(op.lpstrFile[i]=='\0')
        {
            images_selected[imptr++] = '\n';
            break;
        }
        images_selected[imptr++] = op.lpstrFile[i];
    }

    SetWindowText(Selected, images_selected);   // Update contents of the Images Added
}