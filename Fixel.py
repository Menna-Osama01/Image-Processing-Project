import streamlit as st
import numpy as np 
import cv2
from PIL import Image
import io

def power_law_transform(img, gamma):
    normalized_img = img / 255.0
    transformed_img = np.power(normalized_img, gamma)
    transformed_img = np.uint8(transformed_img * 255)
    return transformed_img

def linear_negative(img):
    negative_image=255-img
    return negative_image 

def Thresholding(img,threshold_value,max_value,thresh_type_code):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresholded_image = cv2.threshold(img,threshold_value, max_value, thresh_type_code)
    return thresholded_image

def Morphological_Transformation(img, operation_type,kernel_size,iterations):
    kernel = np.ones((kernel_size,kernel_size),np.uint8)
    if operation_type == "Erosion":
        result = cv2.erode(img, kernel, iterations)
    elif operation_type == "Dilation":
        result = cv2.dilate(img, kernel, iterations)
    elif operation_type == "Opening":
        result = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
    elif operation_type == "Closing":
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) 
    return result
    

def welcome_page():
    st.title(":blue[Welcome to Fixel ] :camera:")
    st.subheader("",divider="gray")
    st.subheader(":blue[Fixel] is a web application that allows you to apply different image processing techniques to enhance and transform your photos.")
    st.subheader("With just a few clicks, you can upload an image and choose from a variety of tools such as :red[Thresholding], :blue[Power-Law (Gamma) Transformation], :green[ Linear Negative], and :violet[Morphological Operations].")
    st.subheader("Try it out and see how simple image processing can create :rainbow[powerful results!]")

def main_page():
    st.title(":blue[Image Enhancement]")
    st.write(":gray[Upload Image]")
    uploaded_file=st.file_uploader("", type=["jpg","png","jpeg"])
    camera_img=st.camera_input("Take a photo")
#upload
    img= None
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
    elif camera_img is not None:
        img = Image.open(camera_img)
#enhance
    if img is not None:
        st.image(img, caption='Original Image')
        img_np=np.array(img)
        if img_np.ndim == 3 and img_np.shape[2] == 3:
            img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        else:
            img_cv = img_np

    enhancement= st.selectbox("Choose Enhancement Technique",["Thresholding", "Linear Negative Transformation", "Power-Law Transformation","Morphological Transformation"])

    if enhancement =="Power-Law Transformation":
         gamma= st.slider("Choose gamma value",min_value=0.1,max_value=5.0 , value=1.0, step=0.1)

    elif enhancement =="Thresholding":
        threshold_value = st.slider("Select threshold value", 0, 255, 100)
        max_value = st.slider("Select max value", 0, 255, 255)
        threshold_type = st.selectbox("Choose Threshold Type",["Binary", "Binary Inverse","Binary using OTSU", "Truncate", "To Zero", "To Zero Inverse"])
        threshold_types = {"Binary": cv2.THRESH_BINARY,
        "Binary Inverse": cv2.THRESH_BINARY_INV,
        "Binary using OTSU":cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        "Truncate": cv2.THRESH_TRUNC,
        "To Zero": cv2.THRESH_TOZERO,
        "To Zero Inverse": cv2.THRESH_TOZERO_INV,}
        thresh_type_code = threshold_types[threshold_type]
    
    elif enhancement =="Morphological Transformation":
        operation_type = st.selectbox("Select Morphological Operation", ["Erosion", "Dilation", "Opening", "Closing"])
        #if operation_type=="Erosion" or operation_type == "Dilation":
        iterations = st.slider("iterations", min_value=1, max_value=30, step=2, value=5)
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=15, step=2, value=5)




    if st.button("Fix Your Pixel"):
        if enhancement =="Power-Law Transformation":
            output=power_law_transform(img_cv, gamma)
        elif enhancement =="Linear Negative Transformation":
            output=linear_negative(img_cv)
        elif enhancement =="Thresholding":
            output=Thresholding(img_cv,threshold_value,max_value,thresh_type_code)
        elif enhancement =="Morphological Transformation":
            output=Morphological_Transformation(img_cv,operation_type,kernel_size,iterations)

        
        output_rgb= cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        original= cv2.cvtColor(img_cv,cv2.COLOR_BGR2RGB)
        col1,col2 =st.columns(2)
        with col1:
            st.image(original, caption="Original Image",use_column_width=True)
        with col2:
            st.image(output_rgb, caption="Enhanced Image",use_column_width=True)

        st.subheader("Download it Now!! :smile:")

        image_pil = Image.fromarray(output_rgb)
        buffer = io.BytesIO()
        image_pil.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
        label="Download image",
        data=buffer,
        file_name="EnhancedImage.png",
        mime="image/png"
    )
        

   

def enhancementmethods_page():
    tab1, tab2, tab3, tab4 = st.tabs(["Thresholding", "Linear Negative Transformation", "Power-Law Transformation","Morphological Transformation"])

    with tab1:
        st.title(":violet[Thresholding]")
        st.subheader("",divider="gray")
        st.subheader(":gray[Thresholding transformations are particularly useful for segmentation in which we want to isolate *an object of interest from a background*]")
        st.header(":violet[When to use Thresholding:]")
        st.header("1.Object Detection:")
        st.subheader(":gray[To isolate objects from the background (e.g., separating a handwritten digit from paper).]")
        st.header("2.Preprocessing for OCR (Optical Character Recognition):")
        st.subheader(":gray[Converts printed or handwritten text into machine-readable form.]")
        st.header("3.Image Simplification:")
        st.subheader(":gray[Reduces image complexity for easier analysis.]")
        st.header("4.Edge Detection (after enhancement):")
        st.subheader(":gray[To highlight the borders of objects.]")
        st.image("ImageProject/thresholded.jpg",width=560)
    with tab2:
        st.title(":violet[Linear Negative Transformation]")
        st.subheader("",divider="gray")
        st.subheader(":gray[Linear negative transformation is an image processing technique that *inverts the grayscale intensities of an image*. It transforms each pixel value r into s using the formula:]")
        st.latex("s = (intensity)max - r")
        st.header(":violet[When to use Linear Negative Transformation:]")
        st.subheader("1.Medical Imaging:")
        st.subheader(":gray[Helps to highlight structures in X-rays or MRI scans by enhancing dark regions.]")
        st.subheader("2.Photographic Negatives:")
        st.subheader(":gray[Used to create negative film effects or restore old negatives.]")
        st.subheader("3.Enhancing Dark Regions:")
        st.subheader(":gray[If the important details are in dark areas, inverting the image can make them more visible.]")
        st.subheader("4.Preprocessing for Feature Extraction:")
        st.subheader(":gray[Sometimes improves the accuracy of edge detection or object recognition algorithms.]")
        st.image("https://cdnintech.com/media/chapter/51312/1512345123/media/fig20.png",width=560)
    with tab3:
        st.title(":violet[Power-Law Transformation:]")
        st.subheader("",divider="gray")
        st.subheader(":gray[Power-law transformation is an image enhancement technique that applies a *nonlinear* adjustment to pixel values *to control brightness and contrast*.]")
        st.latex("s=c*r^γ")
        st.header(":violet[When to use Power-Law Transformation:]")
        st.subheader("1.Adjusting Brightness:")
        st.subheader(":gray[•γ < 1: Brightens dark regions.]")
        st.subheader(":gray[ •γ > 1: Darkens bright regions.]")
        st.subheader("2.Correcting Image Display:") 
        st.subheader(":gray[Used in monitors, cameras, and TVs to correct how images are shown.]")
        st.subheader("3.Preprocessing in Image Analysis:")
        st.subheader("gray[Enhances certain intensity ranges before applying edge detection or segmentation.]")
        st.subheader("4.Improving Visibility:")
        st.subheader(":gray[Helpful for images with poor lighting or uneven brightness.]")
        st.image("ImageProject/power-law.jpg")
    with tab4:
        st.title(":violet[Morphological Transformation:]")
        st.subheader("",divider="gray")
        st.subheader(":gray[Morphological transformations are a set of *operations based on shapes*, usually applied to *binary images*. They process images using a small shape or template called a *structuring element (kernel)*.]")
        st.header(":violet[Common Morphological Operations:]")

        st.subheader("1.Erosion:")
        st.subheader(":gray[Removes white pixels near the edges- makes objects *shrink*.] ")
        st.subheader(":gray[Good for removing small white noise.]")
        st.subheader("2.Dilation:")
        st.subheader(":gray[Adds white pixels to the edges - makes objects *grow*.]")
        st.subheader(":gray[Fills small holes and connects nearby objects.]") 
        st.subheader("3.Opening (Erosion → Dilation):")
        st.subheader(":gray[Removes noise without affecting the shape much.]")
        st.subheader("4.Closing (Dilation → Erosion):")
        st.subheader(":gray[Fills small black holes in white objects.]")
        st.subheader("5.Morphological Gradient:")
        st.subheader(":gray[Highlights edges by subtracting eroded image from dilated image.]")
        st.header(":violet[When to Use Morphological Transformations:]")
        st.subheader(":gray[•Noise removal.]")
        st.subheader(":gray[•Filling holes or gaps.]")
        st.subheader(":gray[•Separating connected objects.]")
        st.subheader(":gray[•Finding object boundaries.]")
        st.subheader(":gray[•Preprocessing before contour detection or OCR.]")
        st.image("https://www.dspguide.com/graphics/F_25_10.gif")





def reach_us_page():
    st.title(":violet[Get in Touch] :star:")
    st.subheader("",divider="gray")
    st.subheader("For any feedback, suggestions, or inquiries, feel free to contact us at:")
    st.subheader(":gray[Outlook:]")
    st.write("- mariam.aly.2024@aiu.edu.eg")
    st.write("- catherine.gaballah.2024@aiu.edu.eg")
    st.write("- mennatallah.khalil.2024@aiu.edu.eg")


def aboutus_page():
    st.title(":violet[Fixel]")
    st.subheader("",divider="gray")
    st.subheader("We are three second-year students at :violet[Alamein International University], working together on a project for the :violet[Image Processing] course as part of our Computer Science studies. Our project is a web application called *:violet[Fixel]*, which is designed to enhance and edit images using digital image processing techniques. Through this project, we aim to apply what we’ve learned in a practical way and gain more experience in software development and image processing.")
    st.image("ImageProject/finallogo.png", caption="Fixel to fix your pixel")




page = st.sidebar.radio(
    "Choose a page :smile: ",
    ("Welcome to Fixel","Fix Your Pixel", "Enhancement Methods", "Reach Us","Our Story")
)

if page== "Fix Your Pixel":
    main_page()
elif page == "Enhancement Methods":
    enhancementmethods_page()
elif page == "Reach Us":
    reach_us_page()
elif page =="Our Story":
    aboutus_page()
elif page== "Welcome to Fixel":
    welcome_page()

