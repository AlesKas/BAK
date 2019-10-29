using CloudApp.handlers;
using CloudApp.models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CloudApp
{
    /// <summary>
    /// Interakční logika pro MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void LoginButton_Click(object sender, RoutedEventArgs e)
        {
            if (String.IsNullOrEmpty(username.Text) || String.IsNullOrEmpty(password.Password))
            {
                MessageBox.Show("Please enter username and password.", "Error", MessageBoxButton.OK);
            }
            else
            {
                SQLhandler handler = new SQLhandler(username.Text, password.Password);
            }
        }

        private void CreateAccount_click(object sender, RoutedEventArgs e)
        {
            Thread newThread = new Thread(new ThreadStart(OpenRegisterWindow));
            newThread.SetApartmentState(ApartmentState.STA);
            newThread.IsBackground = true;
            newThread.Start();
        }

        private void OpenRegisterWindow()
        {
            register reg = new register();
            reg.Show();
            System.Windows.Threading.Dispatcher.Run();
        }

        private void Exit_click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
