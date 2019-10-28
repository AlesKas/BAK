using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
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
                try
                {
                    using (SqlConnection conn = new SqlConnection(@"Data Source=localhost;Initial Catalog=CloudUsers;Integrated Security=True"))
                    {
                        conn.Open();
                        SqlCommand command = new SqlCommand("SELECT * FROM cloud WHERE ");

                        using (SqlDataReader dr = command.ExecuteReader())
                        {
                            while (dr.Read())
                            {

                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Error", MessageBoxButton.OK);
                }
            }
        }
    }
}
