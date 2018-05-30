from redis_io import io
from util import initialize_form_dicts, COLOR_NAMES

FORM_DICTS = dict(
    scatter=dict(
        data_setting=[
            dict(name='x', type='select', value=None, text='Disable', default=0, desc="X Coordinate"),
            dict(name='y', type='select', value=None, text='Disable', default=0, desc="Y Coordinate"),
            dict(name='color', type='select', value=None, text='Disable', default=0, desc="Color"),
            dict(name='size', type='select', value=None, text='Disable', default=0, desc="Size"),
            dict(name='slider', type='select', value=None, text='Disable', default=0, desc="Slider"),
        ],
        config=[
            dict(name='title', type='input', value=None,
                 default='Scatter', desc="Plot Title"),
            dict(name='default_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='orangered', desc="Default Color"),
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='default_size', type='input', value=None,
                 default=6, desc="Default Size"),
            dict(name='n_size', type='select', value=None, item=range(5, 12),
                 default=8, desc="Number of Different Sizes"),
            dict(name='max_size', type='input', value=None, default=10,
                 desc="Maximum Size"),
            dict(name='min_size', type='input', value=None, default=5,
                 desc="Minimum Size"),
            dict(name='palette', type='select', value=None, item=['Inferno256', 'Viridis256'],
                 default='Inferno256', desc="Color Palette"),
            dict(name='shape', type='select', value=None, item=['circle'],
                 default='circle', desc="Dot Shape"),
        ],
        interaction_config=[
            dict(name='slider_function', type='select', value=None, item=['filter', 'selector'],
                 default='filter', desc="Function of the slider"),
            dict(name='slider_name', type='input', value=None,
                 default='slider', desc="Name of the slider"),
            dict(name='slider_start', type='input', value=None,
                 default=0, desc="Minimum Slider Value"),
            dict(name='slider_end', type='input', value=None,
                 default=1, desc="Maximum Slider Value"),
            dict(name='slider_default', type='input', value=None,
                 default=0, desc="Initial Slider Value"),
            dict(name='slider_step', type='input', value=None,
                 default=0.1, desc="Slider Step"),
        ]
    ),
    histogram=dict(
        data_setting=[
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='slider', type='select', value=None, text='Disable', default=0, desc="Slider"),
        ],
        config=[
            dict(name='title', type='input', value=None,
                 default='Histogram', desc="Plot Title"),
            dict(name='fill_color1', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='orangered', desc="Fill Color of Data I"),
            dict(name='fill_color2', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='greenyellow', desc="Fill Color of Data II"),
            dict(name='line_color1', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='red', desc="Line Color of Data I"),
            dict(name='line_color2', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='green', desc="Line Color of Data II"),
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='n_bin', type='input', value=None, default=40,
                 desc="Number of Bins"),
            dict(name='show_pdf1', type='checkbox', value=None,
                 default=True, desc="Show PDF Curve of Data I"),
            dict(name='show_cdf1', type='checkbox', value=None,
                 default=True, desc="Show CDF Curve of Data I"),
            dict(name='show_pdf2', type='checkbox', value=None,
                 default=True, desc="Show PDF Curve of Data II"),
            dict(name='show_cdf2', type='checkbox', value=None,
                 default=True, desc="Show CDF Curve of Data II"),
            dict(name='pdf_color1', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='lightyellow', desc="Color of PDF Curve of Data I"),
            dict(name='cdf_color1', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='lightseagreen', desc="Color of CDF Curve of Data I"),
            dict(name='pdf_color2', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='lightskyblue', desc="Color of PDF Curve of Data II"),
            dict(name='cdf_color2', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='lightpink', desc="Color of CDF Curve of Data II"),
            dict(name='line_width', type='input', value=None,
                 default=4, desc="Line Width of Curves"),
            dict(name='max_probability', type='input', value=None,
                 default=1.0, desc="Maximum Probability Shown on the Axis"),
        ],
        interaction_config=[
            dict(name='slider_function', type='select', value=None, item=['selector'],
                 default='selector', desc="Function of the slider"),
            dict(name='slider_name', type='input', value=None,
                 default='slider', desc="Name of the slider"),
            dict(name='slider_start', type='input', value=None,
                 default=1, desc="Minimum Slider Value"),
            dict(name='slider_end', type='input', value=None,
                 default=1, desc="Maximum Slider Value"),
            dict(name='slider_default', type='input', value=None,
                 default=0, desc="Initial Slider Value"),
            dict(name='slider_step', type='input', value=None,
                 default=0.1, desc="Slider Step"),
            dict(name='max_distinct', type='input', value=None,
                 default=20,  desc="Maximum Number of Distinct Values in Slider's Data"),
        ]
    ),
    line_graph=dict(
        data_setting=[
            dict(name='x', type='select', value=None, text='Disable', default=0, desc="X Coordinate"),
            dict(name='y1', type='select', value=None, text='Disable', default=0, desc="Y Coordinate of Line I"),
            dict(name='y2', type='select', value=None, text='Disable', default=0, desc="Y Coordinate of Line II"),
            dict(name='y3', type='select', value=None, text='Disable', default=0, desc="Y Coordinate of Line III"),
        ],
        config=[
            dict(name='title', type='input', value=None,
                 default='Line Graph', desc="Plot Title"),
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='line_color1', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='orangered', desc="Color of Line I"),
            dict(name='line_color2', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='mediumpurple', desc="Color of Line II"),
            dict(name='line_color3', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='olive', desc="Color of Line III"),
            dict(name='line_dash1', type='select', value=None, item=['solid', 'dashed', 'dotted', 'dotdash', 'dashdot'],
                 default='solid', desc="Line Dash Pattern of Line I"),
            dict(name='line_dash2', type='select', value=None, item=['solid', 'dashed', 'dotted', 'dotdash', 'dashdot'],
                 default='dashed', desc="Line Dash Pattern of Line II"),
            dict(name='line_dash3', type='select', value=None, item=['solid', 'dashed', 'dotted', 'dotdash', 'dashdot'],
                 default='dotted', desc="Line Dash Pattern of Line III"),
            dict(name='line_width1', type='select', value=None, item=range(1, 6),
                 default=3, desc="Line Width of Line I"),
            dict(name='line_width2', type='select', value=None, item=range(1, 6),
                 default=3, desc="Line Width of Line II"),
            dict(name='line_width3', type='select', value=None, item=range(1, 6),
                 default=3, desc="Line Width of Line III"),

        ],
        interaction_config=[
            dict(name='slider_function', type='select', value=None, item=['selector'],
                 default='selector', desc="Function of the slider"),
            dict(name='slider_name', type='input', value=None,
                 default='slider', desc="Name of the slider"),
            dict(name='slider_start', type='input', value=None,
                 default=0, desc="Minimum Slider Value"),
            dict(name='slider_end', type='input', value=None,
                 default=1, desc="Maximum Slider Value"),
            dict(name='slider_default', type='input', value=None,
                 default=0, desc="Initial Slider Value"),
            dict(name='slider_step', type='input', value=None,
                 default=0.1, desc="Slider Step"),
            dict(name='max_distinct', type='input', value=None,
                 default=20, desc="Maximum Number of Distinct Values in Slider's Data"),
        ]
    ),
    scatter_matrix=dict(
        data_setting=[
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='data3', type='select', value=None, text='Disable', default=0, desc="Data III"),
            dict(name='data4', type='select', value=None, text='Disable', default=0, desc="Data IV"),
            dict(name='data5', type='select', value=None, text='Disable', default=0, desc="Data V"),
            dict(name='data6', type='select', value=None, text='Disable', default=0, desc="Data VI"),
            dict(name='data7', type='select', value=None, text='Disable', default=0, desc="Data VII"),
            dict(name='data8', type='select', value=None, text='Disable', default=0, desc="Data VIII"),
            dict(name='data9', type='select', value=None, text='Disable', default=0, desc="Data IX"),
            dict(name='data10', type='select', value=None, text='Disable', default=0, desc="Data X"),
            dict(name='data11', type='select', value=None, text='Disable', default=0, desc="Data XI"),
            dict(name='data12', type='select', value=None, text='Disable', default=0, desc="Data XII"),
            dict(name='data13', type='select', value=None, text='Disable', default=0, desc="Data XIII"),
            dict(name='data14', type='select', value=None, text='Disable', default=0, desc="Data XIV"),
            dict(name='color', type='select', value=None, text='Disable', default=0, desc="Color"),
        ],
        config=[
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='default_dot_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='orangered', desc="Default Dot Color"),
            dict(name='n_color', type='select', value=None, item=range(5, 12),
                 default=8, desc="Number of Different Colors"),
            dict(name='palette', type='select', value=None, item=['Inferno256', 'Viridis256'],
                 default='Inferno256', desc="Color Palette"),
            dict(name='fig_size_x', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size X"),
            dict(name='fig_size_y', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size Y"),
            dict(name='label_font_size', type='select', value=None, item=range(6, 16),
                 default=10, desc="Label Size"),
            dict(name='tick_font_size', type='select', value=None, item=range(4, 12),
                 default=8, desc="Tick Size"),
            dict(name='marker_s', type='select', value=None, item=range(4, 40),
                 default=20, desc="Marker S (Size Para)"),
        ]
    ),
    stacked_bar=dict(
        data_setting=[
            dict(name='by', type='select', value=None, text='Disable', default=0, desc="Labeled or Grouped By"),
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='data3', type='select', value=None, text='Disable', default=0, desc="Data III"),
            dict(name='data4', type='select', value=None, text='Disable', default=0, desc="Data IV"),
        ],
        config=[
            dict(name='title', type='input', value=None,
                 default='Stacked Bar', desc="Plot Title"),
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='fig_size_x', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size X"),
            dict(name='fig_size_y', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size Y"),
            dict(name='title_font_size', type='select', value=None, item=range(12, 30),
                 default=16, desc="Title Font Size"),
            dict(name='label_font_size', type='select', value=None, item=range(10, 24),
                 default=14, desc="Label Size"),
            dict(name='tick_font_size', type='select', value=None, item=range(6, 18),
                 default=8, desc="Tick Size"),
            dict(name='legend_font_size', type='select', value=None, item=range(6, 18),
                 default=10, desc="Legend Font Size"),
            dict(name='is_horizontal', type='checkbox', value=None,
                 default=False, desc="Horizontal"),
            dict(name='group_by', type='checkbox', value=None,
                 default=False, desc="Group by Data"),
        ]
    ),
    box_plot=dict(
        data_setting=[
            dict(name='by', type='select', value=None, text='Disable', default=0, desc="Labeled or Grouped By"),
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='data3', type='select', value=None, text='Disable', default=0, desc="Data III"),
            dict(name='data4', type='select', value=None, text='Disable', default=0, desc="Data IV"),
            dict(name='data5', type='select', value=None, text='Disable', default=0, desc="Data V"),
            dict(name='data6', type='select', value=None, text='Disable', default=0, desc="Data VI"),
            dict(name='data7', type='select', value=None, text='Disable', default=0, desc="Data VII"),
            dict(name='data8', type='select', value=None, text='Disable', default=0, desc="Data VIII"),
            dict(name='data9', type='select', value=None, text='Disable', default=0, desc="Data IX"),
            dict(name='data10', type='select', value=None, text='Disable', default=0, desc="Data X"),
            dict(name='data11', type='select', value=None, text='Disable', default=0, desc="Data XI"),
            dict(name='data12', type='select', value=None, text='Disable', default=0, desc="Data XII"),
            dict(name='data13', type='select', value=None, text='Disable', default=0, desc="Data XIII"),
            dict(name='data14', type='select', value=None, text='Disable', default=0, desc="Data XIV"),
        ],
        config=[
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='fig_size_x', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size X"),
            dict(name='fig_size_y', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size Y"),
            dict(name='xtick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="X Tick Size"),
            dict(name='ytick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="Y Tick Size"),
            dict(name='box_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='darkolivegreen', desc="Box Color"),
            dict(name='whisker_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='orangered', desc="Whisker Color"),
            dict(name='median_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='darkslateblue', desc="Median Color"),
            dict(name='cap_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='darkslategray', desc="Cap Color"),
        ]
    ),
    andrews_curves=dict(
        data_setting=[
            dict(name='by', type='select', value=None, text='Disable', default=0, desc="Labeled or Grouped By"),
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='data3', type='select', value=None, text='Disable', default=0, desc="Data III"),
            dict(name='data4', type='select', value=None, text='Disable', default=0, desc="Data IV"),
            dict(name='data5', type='select', value=None, text='Disable', default=0, desc="Data V"),
            dict(name='data6', type='select', value=None, text='Disable', default=0, desc="Data VI"),
            dict(name='data7', type='select', value=None, text='Disable', default=0, desc="Data VII"),
            dict(name='data8', type='select', value=None, text='Disable', default=0, desc="Data VIII"),
            dict(name='data9', type='select', value=None, text='Disable', default=0, desc="Data IX"),
            dict(name='data10', type='select', value=None, text='Disable', default=0, desc="Data X"),
            dict(name='data11', type='select', value=None, text='Disable', default=0, desc="Data XI"),
            dict(name='data12', type='select', value=None, text='Disable', default=0, desc="Data XII"),
            dict(name='data13', type='select', value=None, text='Disable', default=0, desc="Data XIII"),
            dict(name='data14', type='select', value=None, text='Disable', default=0, desc="Data XIV"),
        ],
        config=[
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='n_color', type='select', value=None, item=range(5, 12),
                 default=8, desc="Number of Different Colors"),
            dict(name='palette', type='select', value=None, item=['Inferno256', 'Viridis256'],
                 default='Inferno256', desc="Color Palette"),
            dict(name='fig_size_x', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size X"),
            dict(name='fig_size_y', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size Y"),
            dict(name='xtick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="X Tick Size"),
            dict(name='ytick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="Y Tick Size"),
            dict(name='line_width', type='select', value=None, item=[float(x)/10 for x in range(2, 30, 4)],
                 default=1.0, desc="Line Width"),
        ]
    ),
    radviz=dict(
        data_setting=[
            dict(name='by', type='select', value=None, text='Disable', default=0, desc="Labeled or Grouped By"),
            dict(name='data1', type='select', value=None, text='Disable', default=0, desc="Data I"),
            dict(name='data2', type='select', value=None, text='Disable', default=0, desc="Data II"),
            dict(name='data3', type='select', value=None, text='Disable', default=0, desc="Data III"),
            dict(name='data4', type='select', value=None, text='Disable', default=0, desc="Data IV"),
            dict(name='data5', type='select', value=None, text='Disable', default=0, desc="Data V"),
            dict(name='data6', type='select', value=None, text='Disable', default=0, desc="Data VI"),
            dict(name='data7', type='select', value=None, text='Disable', default=0, desc="Data VII"),
            dict(name='data8', type='select', value=None, text='Disable', default=0, desc="Data VIII"),
            dict(name='data9', type='select', value=None, text='Disable', default=0, desc="Data IX"),
            dict(name='data10', type='select', value=None, text='Disable', default=0, desc="Data X"),
            dict(name='data11', type='select', value=None, text='Disable', default=0, desc="Data XI"),
            dict(name='data12', type='select', value=None, text='Disable', default=0, desc="Data XII"),
            dict(name='data13', type='select', value=None, text='Disable', default=0, desc="Data XIII"),
            dict(name='data14', type='select', value=None, text='Disable', default=0, desc="Data XIV"),
        ],
        config=[
            dict(name='background_color', type='select', value=None, item=list(COLOR_NAMES.keys()),
                 default='whitesmoke', desc="Background Color"),
            dict(name='n_color', type='select', value=None, item=range(5, 12),
                 default=8, desc="Number of Different Colors"),
            dict(name='palette', type='select', value=None, item=['Inferno256', 'Viridis256'],
                 default='Inferno256', desc="Color Palette"),
            dict(name='fig_size_x', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size X"),
            dict(name='fig_size_y', type='select', value=None, item=range(2, 16),
                 default=7, desc="Figure Size Y"),
            dict(name='xtick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="X Tick Size"),
            dict(name='ytick_font_size', type='select', value=None, item=range(8, 18),
                 default=10, desc="Y Tick Size"),
            dict(name='marker_s', type='select', value=None, item=range(1, 40),
                 default=20, desc="Marker S (Size Para)"),
        ]
    ),
)


def check_plot_type(plot_type):
    return plot_type in list(FORM_DICTS.keys())


def load_selected_frame_id(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    selected_frame_id = io.load(plot_type+'_selected_frame_id')
    return selected_frame_id


def save_selected_frame_id(plot_type, selected_frame_id):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    io.save(plot_type + '_selected_frame_id', selected_frame_id)


def initialize_forms(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    data_setting = initialize_form_dicts(FORM_DICTS[plot_type]['data_setting'])
    config = initialize_form_dicts(FORM_DICTS[plot_type]['config'])
    io.save(plot_type+'_data_setting', data_setting)
    io.save(plot_type+'_config', config)
    if 'interaction_config' in FORM_DICTS[plot_type]:
        interaction_config = initialize_form_dicts(FORM_DICTS[plot_type]['interaction_config'])
        io.save(plot_type+'_interaction_config', interaction_config)


def load_forms(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    data_setting = io.load(plot_type+'_data_setting')
    config = io.load(plot_type+'_config')
    interaction_config = io.load(plot_type+'_interaction_config')
    if data_setting is None or config is None:
        raise ValueError("Cannot load forms from redis, cache missing")
    if interaction_config is None:
        return data_setting, config
    else:
        return data_setting, config, interaction_config


def load_data_setting(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    data_setting = io.load(plot_type + '_data_setting')
    if data_setting is None:
        raise ValueError("Cannot load forms from redis, cache missing")
    return data_setting


def load_config(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    config = io.load(plot_type + '_config')
    if config is None:
        raise ValueError("Cannot load forms from redis, cache missing")
    return config


def load_interaction_config(plot_type):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    interaction_config = io.load(plot_type + '_interaction_config')
    if interaction_config is None:
        raise ValueError("Cannot load forms from redis, cache missing")
    return interaction_config


def save_data_setting(plot_type, data_setting):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    io.save(plot_type + '_data_setting', data_setting)


def save_config(plot_type, config):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    io.save(plot_type + '_config', config)


def save_interaction_config(plot_type, interaction_config):
    if not check_plot_type(plot_type):
        raise ValueError("Invalid Plot Type")
    io.save(plot_type + '_interaction_config', interaction_config)