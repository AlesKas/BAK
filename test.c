// gcc -Wall -Wextra -o Ex1 Ex1.c $(pkg-config gtk+-3.0 --cflags --libs)
#include <stdlib.h>
#include <stdio.h>
#include <gtk/gtk.h>

int main(int argc,char **argv) 
{
    GtkWidget *window;
    gtk_init(&argc , &argv);
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_widget_show_all(window);
    gtk_main();
    return;
}