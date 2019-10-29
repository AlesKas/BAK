using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CloudApp.models
{
    class User
    {
        private int Id { get; }
        public string username { get; internal set; }
        public string password { get; internal set; }
        public bool admin { get; internal set; }
        public string firstName { get; internal set; }
        public string lastName { get; internal set; }
        public string email { get; internal set; }
    }
}
