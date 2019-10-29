using CloudApp.handlers;
using CloudApp.models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mail;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace CloudApp
{
    /// <summary>
    /// Interakční logika pro register.xaml
    /// </summary>
    public partial class register : Window
    {
        public register()
        {
            InitializeComponent();
            initTextBoxes();
        }

        private void initTextBoxes()
        {
            textBoxFirstName.Text = String.Empty;
            textBoxLastName.Text = String.Empty;
            textBoxUsername.Text = String.Empty;
            textBoxEmail.Text = String.Empty;
            passwordBox1.Password = String.Empty;
            passwordBoxConfirm.Password = String.Empty;
        }

        private bool isValidEmail(string emailAddress)
        {
            return RegexHandler.IsValidEmail(emailAddress);
        }

        private void Submit_Click(object sender, RoutedEventArgs e)
        {
            
            if (String.IsNullOrEmpty(textBoxFirstName.Text) || String.IsNullOrEmpty(textBoxLastName.Text))
            {
                MessageBox.Show("Please enter your name and surname.", "Error", MessageBoxButton.OK);
            }
            if (String.IsNullOrEmpty(textBoxUsername.Text))
            {
                MessageBox.Show("Please enter your username.", "Error", MessageBoxButton.OK);
            }
            else if (!isValidEmail(textBoxEmail.Text))
            {
                MessageBox.Show("Please enter valid email address.", "Error", MessageBoxButton.OK);
            }
            else if (passwordBox1.Password != passwordBoxConfirm.Password)
            {
                MessageBox.Show("Password does not match.", "Error", MessageBoxButton.OK);
            }
            else
            {
                SQLhandler sql = new SQLhandler();
                if (sql.isUsernameAvailable(textBoxUsername.Text))
                {
                    createUser();
                }
                else
                {
                    MessageBox.Show("Username is already used.", "Error", MessageBoxButton.OK);
                }
            }
            
        }

        private bool createUser()
        {
            User user = new User();
            user.firstName = textBoxFirstName.Text;
            user.lastName = textBoxLastName.Text;
            user.username = textBoxUsername.Text;
            user.admin = false;
            user.email = textBoxEmail.Text;
            user.password = passwordBox1.Password;
            return new SQLhandler().createUser(user);
        }

        private void button2_Click(object sender, RoutedEventArgs e)
        {
            initTextBoxes();
        }

        private void button3_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
    }
}
