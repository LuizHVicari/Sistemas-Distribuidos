#include <iostream>
#include <fstream>
#include <cmath>

#define ITER 4000
#define DIMEN 4000

using namespace std;

const int width = DIMEN, height = DIMEN;
const double x_min = -2.5, x_max = 1.5, y_min = -2.0, y_max = 2.0;
const int max_iter = ITER;
const double escape_radius = 2.0;

int main()
{
    ofstream img("mandelbrot_serial.ppm");
    // img << "P3\n" << width << " " << height << "\n255 0 \n"; // define o cabeçalho PPM

    int bg_red = 255, bg_green = 255, bg_blue = 255; // define a cor de fundo branca

    for (int y = 0; y < height; ++y)
    {
        double c_im = y_min + (y * (y_max - y_min) / height);

        if (fabs(c_im) < 1e-6)
        {
            c_im = 0.0; // converge to the real axis
        }

        for (int x = 0; x < width; ++x)
        {
            double c_re = x_min + (x * (x_max - x_min) / width);
            double z_re = c_re, z_im = c_im;
            bool in_set = true;

            for (int i = 0; i < max_iter; ++i)
            {
                double z_re2 = z_re * z_re, z_im2 = z_im * z_im;

                if (z_re2 + z_im2 > escape_radius * escape_radius)
                {
                    in_set = false;
                    break;
                }

                z_im = 2 * z_re * z_im + c_im;
                z_re = z_re2 - z_im2 + c_re;
            }

            if (in_set)
            {
                // img << "255 255 255 "; // cor do pixel de fundo
            }
            else
            {
                // calcular a cor do fractal com base nas coordenadas x e y
                int iter = 0;
                double z_re = c_re, z_im = c_im;
                while (iter < max_iter && (z_re * z_re + z_im * z_im) < escape_radius * escape_radius) {
                    double z_re_new = z_re * z_re - z_im * z_im + c_re;
                    double z_im_new = 2 * z_re * z_im + c_im;
                    z_re = z_re_new;
                    z_im = z_im_new;
                    iter++;
                }
                if (iter == max_iter) {
                    // img << bg_red << " " << bg_green << " " << bg_blue << " ";
                } else {
                    int red = (int)(255 * (iter % 64) / 63.0);
                    int green = (int)(255 * (iter % 32) / 31.0);
                    int blue = (int)(255 * (iter % 16) / 15.0);
                    // img << red << " " << green << " " << blue << " ";
                }
            }
        }

        img << "\n";
    }

    img.close();

    return 0;
}
