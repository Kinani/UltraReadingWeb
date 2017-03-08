using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(UltraReadingWeb.Startup))]
namespace UltraReadingWeb
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
