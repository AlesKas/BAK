#pragma once

#ifdef _WIN64
	#include "wx/wx.h"
#elif __linux__
	#include <wx-3.1/wx/wx.h>
#endif
#include "cMain.h"

class cApp : public wxApp
{

public:	
	cApp();
	~cApp();
	virtual bool OnInit();
private:
	cMain* frame1 = nullptr;

};

