#pragma once
#ifdef _WIN64
	#include "wx/wx.h"
#elif __linux__
	#include <wx-3.1/wx/wx.h>
#endif
#include "cMain.h"


class cMain : public wxFrame
{
public:
	cMain();
	~cMain();
};

