from django.views import generic
from django.shortcuts import get_object_or_404, render,HttpResponse
from .models import Post,Category
from django.views.generic.detail import DetailView
from .forms import commentform
from django.core.mail import send_mail
from django.contrib import messages
from mypage.models import Page
from .forms import contactform


def homepage(request):
    queryset = Post.objects.filter(status=1).order_by('-created')
    cat_title= Category.objects.all()
    newpages=Page.objects.all()
    page_one=Page.objects.filter(title__contains='about')
    page_two=Page.objects.filter(title__contains='cloud')
    form=contactform()
   

    if request.method=='POST':
        form=contactform(request.POST)

        if form.is_valid():
            Name = form.cleaned_data["name"]
            Message = form.cleaned_data["message"]
            Email = form.cleaned_data["email"]

            send_mail(
            Name,Message,Email,['kshitizbasnet86@gmail.com']

            )
            form=contactform()
            messages.success(request,'message sent succesfully',fail_silently=True)
            return render(request,'post/index.html',{'queryset':queryset,'cat_title':cat_title,'form':form})
       
    else:
        form=contactform()
    
    return render(request,'post/index.html',{'queryset':queryset,'cat_title':cat_title,'newpages':newpages,'page_one':page_one,'page_two':page_two,'form':form})




def categoryview(request,cat_name):
    category = get_object_or_404(Category, slug=cat_name)
    cat_post = Post.objects.filter(category=category)
    cat_title= Category.objects.all()
    return render(request,'post/category.html',{'category':category,'cat_post':cat_post,'cat_title':cat_title})

def PostDetail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments=post.comments.all().order_by('-created')
    new_comment = None

    if request.method == 'POST':
        comment_form = commentform(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
            comment_form = commentform()

    return render(request, 'post/detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,'comment_form':comment_form})



