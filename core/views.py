from django.shortcuts import render, get_object_or_404, render_to_response
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from core.models import Candidate, CandidateMeanSentiment
from math import pi
from django.db.models import Min, Max
from datetime import timedelta, datetime

def index(request):
    color_list = []
    sentiment_list = []
    candidates_list = []
    candidates_sentiments_dict = {}
    candidates = Candidate.objects.all()
    candidate_accordian_list = []
    for candidate in candidates:
        mean_sentiment_min_from = CandidateMeanSentiment.objects.filter(candidate = candidate).aggregate(Min('from_date_time'))
        mean_sentiment_max_to = CandidateMeanSentiment.objects.filter(candidate = candidate).aggregate(Max('to_date_time'))
        print(candidate)
        print(mean_sentiment_max_to)
        print(mean_sentiment_min_from)
        # breakpoint()
        total_mean_sentiment = CandidateMeanSentiment.objects.filter(
            candidate = candidate,
            from_date_time = mean_sentiment_min_from['from_date_time__min'],
            to_date_time = mean_sentiment_max_to['to_date_time__max'],
        )
        # print(total_mean_sentiment)
        # breakpoint()
        if total_mean_sentiment[0].mean_sentiment > 0.009 or total_mean_sentiment[0].mean_sentiment < -.009:
            candidates_sentiments_dict[str(candidate)] = [total_mean_sentiment[0].mean_sentiment]
            if candidate.party == 'democrat':
                candidates_sentiments_dict[str(candidate)].append('#415caa')
            elif candidate.party == 'republican':
                candidates_sentiments_dict[str(candidate)].append('#ed2024')
            else:
                candidates_sentiments_dict[str(candidate)].append('#696969')
        if total_mean_sentiment[0].mean_sentiment > .125:
            candidate_accordian_list.append(candidate)
    candidates_list = list(candidates_sentiments_dict.  keys())
    sentiment_color_list = candidates_sentiments_dict.values()
    for sentiment_color in sentiment_color_list:
        sentiment_list.append(sentiment_color[0])
        color_list.append(sentiment_color[1])

    source = ColumnDataSource(data=dict(candidates_list=candidates_list, sentiment_list=sentiment_list, color=color_list))
    plot = figure(x_range=candidates_list, y_range=(-0.5, .5),
                  x_axis_label='Candidates', y_axis_label='Sentiment',
                  plot_height=500, plot_width=800, title="Mean Sentiment Per Candidate",
                  tools="", toolbar_location=None,)
    plot.vbar(x='candidates_list', top='sentiment_list', width=0.4,color='color', source=source)
    plot.xaxis.major_label_orientation = pi/4
    plot.xgrid.grid_line_color = None
    # plot.legend.orientation = "vertical"
    # plot.legend.location = "top_center"
    script, div = components(plot)
    context = {'script': script, 'div': div, 'candidates': candidates, 'candidate_accordian_list': candidate_accordian_list}
    return render_to_response('index.html', context=context)

def candidates(request):
    candidates = Candidate.objects.all()

    return render(request, "candidates.html",
                  context={'candidates': candidates})


def candidate_detail(request, slug):
    candidate = get_object_or_404(Candidate, slug=slug)
    # color_list = []
    # sentiment_list = []
    # candidates_list = []
    # candidates_sentiments_dict = {}
    # candidate = Candidate.objects.get(Candidate, id=id)
    candidates = Candidate.objects.all()
    
    agg_mean_sentiments = []
    agg_mean_sentiment_dates = []
    daily_mean_sentiments = []
    daily_mean_sentiment_dates = []
    mean_sentiment_min_from = CandidateMeanSentiment.objects.filter(candidate = candidate).aggregate(Min('from_date_time'))
    min_time = mean_sentiment_min_from['from_date_time__min']

    utcnow = datetime.utcnow()

    day_delta = utcnow.day - min_time.day


    for day in range(day_delta):
        daily_sentiment = CandidateMeanSentiment.objects.filter(
            candidate = candidate,
            from_date_time = min_time + timedelta(days=day),
            to_date_time = min_time + timedelta(days=day+1)
        )
        if daily_sentiment:
            daily_mean_sentiment_dates.append(daily_sentiment[0].to_date_time)
            daily_mean_sentiments.append(daily_sentiment[0].mean_sentiment)




    agg_candidate_mean_sentiments = CandidateMeanSentiment.objects.filter(
        candidate = candidate,
        from_date_time = mean_sentiment_min_from['from_date_time__min']
    )



    # daily_candidate_mean_sentiments = CandidateMeanSentiment.objects.filter(
    #     candidate=candidate
    # ).annotate(
    #     delta = F('to_date_time') - F('from_date_time')
    # ).filter(
    #     delta = timedelta(days=1, hours=0, minutes=0)
    # )
    # print(daily_candidate_mean_sentiments)

    # daily_mean_sentiments = CandidateMeanSentiment.objects.filter(
    #     candidate = candidate,
    # )
    # print(agg_mean_sentiments)
    # breakpoint()



    for mean_sentiment in agg_candidate_mean_sentiments:
        agg_mean_sentiments.append(mean_sentiment.mean_sentiment)
        agg_mean_sentiment_dates.append(mean_sentiment.to_date_time)
        
    # print(mean_sentiments)
    # breakpoint()
    # data = {'date': mean_sentiment_dates,
    #         'sentiment': mean_sentiments}
    # source = ColumnDataSource(data)
    detail_line_graph = figure(x_axis_label='Date of sentiment',
                  x_axis_type='datetime',
                  y_axis_label='Sentiment',
                  plot_width=1000,
                  plot_height=500,
                  toolbar_location=None,
                  y_range=(-0.5, 0.5))
    detail_line_graph.multi_line([agg_mean_sentiment_dates, daily_mean_sentiment_dates], [agg_mean_sentiments, daily_mean_sentiments], color=['black', 'blue'],line_width=4, alpha=[.8, .5])
    # detail_line_graph.xaxis.major_label_orientation = pi/4
    # print(mean_sentiments)
    # print(mean_sentiment_dates)
    # comparison_line_graph = figure()
    # comparison_line_graph.wedge()

    # plot3 = figure()
    # plot3.comparisonview


    script, div = components(detail_line_graph)
    context = {'script': script, 'div': div, 'candidate': candidate, 'candidates': candidates}
    return render_to_response('candidate_detail.html', context=context)


def methodology(request):
    candidates = Candidate.objects.all()

                  
    return render(request, "methodology.html", context={'candidates': candidates})


def about(request):
    candidates = Candidate.objects.all()

    return render(request, "about.html", context={'candidates': candidates})
